/*
 *  Copyright 2023 Collate.
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *  http://www.apache.org/licenses/LICENSE-2.0
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import {
  mockActiveAnnouncementData,
  mockCustomizePageClassBase,
  mockDocumentData,
  mockPersonaName,
  mockUserData,
} from '../../mocks/MyDataPage.mock';
import { getDocumentByFQN } from '../../rest/DocStoreAPI';
import { getActiveAnnouncement } from '../../rest/feedsAPI';
import MyDataPage from './MyDataPage.component';

const mockLocalStorage = (() => {
  let store: Record<string, string> = {};

  return {
    getItem(key: string) {
      return store[key] || '';
    },
    setItem(key: string, value: string) {
      store[key] = value.toString();
    },
    clear() {
      store = {};
    },
  };
})();

Object.defineProperty(window, 'localStorage', {
  value: mockLocalStorage,
});

jest.mock('../../components/common/Loader/Loader', () => {
  return jest.fn().mockImplementation(() => <div>Loader</div>);
});
jest.mock('../../utils/CustomizeMyDataPageClassBase', () => {
  return mockCustomizePageClassBase;
});
jest.mock('../../components/PageLayoutV1/PageLayoutV1', () => {
  return jest
    .fn()
    .mockImplementation(({ children }) => (
      <div data-testid="page-layout-v1">{children}</div>
    ));
});
jest.mock(
  '../../components/MyData/WelcomeScreen/WelcomeScreen.component',
  () => {
    return jest
      .fn()
      .mockImplementation(({ onClose }) => (
        <div onClick={onClose}>WelcomeScreen</div>
      ));
  }
);

let mockSelectedPersona: Record<string, string> | null = {
  fullyQualifiedName: mockPersonaName,
};

jest.mock('../../hooks/useApplicationStore', () => ({
  useApplicationStore: jest.fn().mockImplementation(() => ({
    currentUser: mockUserData,
    selectedPersona: mockSelectedPersona,
  })),
}));

jest.mock('../../hooks/useGridLayoutDirection', () => ({
  useGridLayoutDirection: jest.fn().mockImplementation(() => 'ltr'),
}));

jest.mock('../../rest/DocStoreAPI', () => ({
  getDocumentByFQN: jest
    .fn()
    .mockImplementation(() => Promise.resolve(mockDocumentData)),
}));
jest.mock('../../rest/feedsAPI', () => ({
  getActiveAnnouncement: jest
    .fn()
    .mockImplementation(() => Promise.resolve(mockActiveAnnouncementData)),
}));
jest.mock('../../rest/userAPI', () => ({
  getUserById: jest
    .fn()
    .mockImplementation(() => Promise.resolve(mockUserData)),
}));
jest.mock('../../hooks/useCustomLocation/useCustomLocation', () => {
  return jest.fn().mockImplementation(() => ({ pathname: '' }));
});
jest.mock('../../rest/searchAPI', () => {
  return {
    searchQuery: jest
      .fn()
      .mockImplementation(() =>
        Promise.resolve({ hits: { hits: [], total: { value: 0 } } })
      ),
  };
});
jest.mock('react-grid-layout', () => ({
  ...jest.requireActual('react-grid-layout'),
  WidthProvider: jest
    .fn()
    .mockImplementation(() =>
      jest
        .fn()
        .mockImplementation(({ children }) => (
          <div data-testid="react-grid-layout">{children}</div>
        ))
    ),
  __esModule: true,
  default: '',
}));

jest.mock('../../hoc/LimitWrapper', () => {
  return jest
    .fn()
    .mockImplementation(({ children }) => <>LimitWrapper{children}</>);
});

jest.mock('../DataInsightPage/DataInsightProvider', async () => {
  return jest.fn().mockImplementation(({ children }) => <>{children}</>);
});

jest.mock('../../hooks/useWelcomeStore', () => ({
  useWelcomeStore: jest.fn().mockReturnValue({
    isWelcomeVisible: true,
  }),
}));

jest.mock('../../components/AppRouter/withActivityFeed', () => ({
  withActivityFeed: jest.fn().mockImplementation((Component) => Component),
}));

jest.mock('../DataInsightPage/DataInsightProvider', () => {
  return {
    __esModule: true,
    default: jest.fn().mockImplementation(({ children }) => <>{children}</>),
    useDataInsightProvider: jest.fn().mockReturnValue({
      kpi: {
        isLoading: false,
        data: [],
      },
    }),
  };
});

describe('MyDataPage component', () => {
  beforeEach(() => {
    localStorage.setItem('loggedInUsers', mockUserData.name);
  });

  it('MyDataPage should only display WelcomeScreen when user logs in for the first time', async () => {
    // Simulate no user is logged in condition
    localStorage.clear();

    render(<MyDataPage />);

    expect(await screen.findByText('WelcomeScreen')).toBeInTheDocument();
  });

  it('MyDataPage should display the main content after the WelcomeScreen is closed', async () => {
    // Simulate no user is logged in condition
    localStorage.clear();

    render(<MyDataPage />);

    const welcomeScreen = await screen.findByText('WelcomeScreen');

    expect(welcomeScreen).toBeInTheDocument();

    userEvent.click(welcomeScreen);

    expect(await screen.findByTestId('react-grid-layout')).toBeInTheDocument();
    expect(screen.queryByText('WelcomeScreen')).toBeNull();
  });

  it('MyDataPage should display loader initially while loading data', async () => {
    render(<MyDataPage />);

    expect(screen.getByText('Loader')).toBeInTheDocument();
    expect(screen.queryByTestId('react-grid-layout')).toBeNull();

    expect(screen.queryByText('WelcomeScreen')).toBeNull();
  });

  it('MyDataPage should display all the widgets in the config and the announcements widget if there are announcements', async () => {
    render(<MyDataPage />);

    expect(
      await screen.findByText('KnowledgePanel.ActivityFeed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Following')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.RecentlyViewed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Announcements')
    ).toBeInTheDocument();
    expect(screen.queryByText('KnowledgePanel.KPI')).toBeNull();
    expect(screen.queryByText('KnowledgePanel.TotalAssets')).toBeNull();
    expect(screen.queryByText('KnowledgePanel.MyData')).toBeNull();
  });

  it('MyDataPage should not render announcement widget if there are no announcements', async () => {
    (getActiveAnnouncement as jest.Mock).mockImplementationOnce(() =>
      Promise.resolve({
        ...mockActiveAnnouncementData,
        data: [],
      })
    );
    render(<MyDataPage />);

    expect(
      await screen.findByText('KnowledgePanel.ActivityFeed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Following')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.RecentlyViewed')
    ).toBeInTheDocument();
    expect(screen.queryByText('KnowledgePanel.Announcements')).toBeNull();
    expect(screen.queryByText('KnowledgePanel.KPI')).toBeNull();
    expect(screen.queryByText('KnowledgePanel.TotalAssets')).toBeNull();
    expect(screen.queryByText('KnowledgePanel.MyData')).toBeNull();
  });

  it('MyDataPage should render default widgets when getDocumentByFQN API fails', async () => {
    (getDocumentByFQN as jest.Mock).mockImplementationOnce(() =>
      Promise.reject(new Error('API failure'))
    );
    render(<MyDataPage />);

    expect(
      await screen.findByText('KnowledgePanel.ActivityFeed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.RecentlyViewed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Following')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Announcements')
    ).toBeInTheDocument();
    expect(await screen.findByText('KnowledgePanel.KPI')).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.TotalAssets')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.MyData')
    ).toBeInTheDocument();
  });

  it('MyDataPage should render default widgets when there is no selected persona', async () => {
    mockSelectedPersona = null;
    render(<MyDataPage />);

    expect(
      await screen.findByText('KnowledgePanel.ActivityFeed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.RecentlyViewed')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Following')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.Announcements')
    ).toBeInTheDocument();
    expect(await screen.findByText('KnowledgePanel.KPI')).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.TotalAssets')
    ).toBeInTheDocument();
    expect(
      await screen.findByText('KnowledgePanel.MyData')
    ).toBeInTheDocument();
  });
});
