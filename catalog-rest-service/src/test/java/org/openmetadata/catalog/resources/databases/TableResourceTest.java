package org.openmetadata.catalog.resources.databases;

import com.fasterxml.jackson.core.JsonProcessingException;
import org.openmetadata.catalog.type.ColumnJoin;
import org.openmetadata.catalog.type.JoinedWith;
import org.openmetadata.catalog.type.TableData;
import org.openmetadata.catalog.type.TableJoins;
import org.apache.http.client.HttpResponseException;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Order;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInfo;
import org.junit.jupiter.api.TestMethodOrder;
import org.openmetadata.catalog.CatalogApplicationTest;
import org.openmetadata.catalog.Entity;
import org.openmetadata.catalog.api.data.CreateDatabase;
import org.openmetadata.catalog.api.data.CreateTable;
import org.openmetadata.catalog.api.services.CreateDatabaseService;
import org.openmetadata.catalog.api.services.CreateDatabaseService.DatabaseServiceType;
import org.openmetadata.catalog.entity.data.Database;
import org.openmetadata.catalog.entity.data.Table;
import org.openmetadata.catalog.entity.services.DatabaseService;
import org.openmetadata.catalog.entity.teams.Team;
import org.openmetadata.catalog.entity.teams.User;
import org.openmetadata.catalog.exception.CatalogExceptionMessage;
import org.openmetadata.catalog.resources.databases.TableResource.TableList;
import org.openmetadata.catalog.resources.services.DatabaseServiceResourceTest;
import org.openmetadata.catalog.resources.tags.TagResourceTest;
import org.openmetadata.catalog.resources.teams.TeamResourceTest;
import org.openmetadata.catalog.resources.teams.UserResourceTest;
import org.openmetadata.catalog.type.Column;
import org.openmetadata.catalog.type.ColumnDataType;
import org.openmetadata.catalog.type.EntityReference;
import org.openmetadata.catalog.type.TableConstraint;
import org.openmetadata.catalog.type.TableConstraint.ConstraintType;
import org.openmetadata.catalog.type.TableType;
import org.openmetadata.catalog.type.TagLabel;
import org.openmetadata.catalog.util.EntityUtil;
import org.openmetadata.catalog.util.EntityUtil.Fields;
import org.openmetadata.catalog.util.JsonUtils;
import org.openmetadata.catalog.util.RestUtil;
import org.openmetadata.catalog.util.TestUtils;
import org.openmetadata.common.utils.CommonUtil;
import org.openmetadata.common.utils.JsonSchemaUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.json.JsonPatch;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.Response.Status;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.UUID;

import static java.util.Collections.singletonList;
import static javax.ws.rs.core.Response.Status.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.openmetadata.catalog.util.RestUtil.DATE_FORMAT;
import static org.openmetadata.catalog.util.TestUtils.assertEntityPagination;
import static org.openmetadata.catalog.util.TestUtils.assertResponse;

@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class TableResourceTest extends CatalogApplicationTest {
  private static final Logger LOG = LoggerFactory.getLogger(TableResourceTest.class);
  public static Database DATABASE;
  public static final TagLabel USER_ADDRESS_TAG_LABEL = new TagLabel().withTagFQN("User.Address");
  public static final TagLabel USER_BANK_ACCOUNT_TAG_LABEL = new TagLabel().withTagFQN("User.BankAccount");

  public static List<Column> COLUMNS =
          Arrays.asList(new Column().withName("c1").withColumnDataType(ColumnDataType.BIGINT).withTags(singletonList(USER_ADDRESS_TAG_LABEL)),
          new Column().withName("c2").withColumnDataType(ColumnDataType.BIGINT).withTags(singletonList(USER_ADDRESS_TAG_LABEL)),
          new Column().withName("c3").withColumnDataType(ColumnDataType.BIGINT).withTags(singletonList(USER_BANK_ACCOUNT_TAG_LABEL)));

  public static User USER1;
  public static EntityReference USER_OWNER1;
  public static Team TEAM1;
  public static EntityReference TEAM_OWNER1;
  public static EntityReference SNOWFLAKE_REFERENCE;

  @BeforeAll
  public static void setup(TestInfo test) throws HttpResponseException {
    CreateDatabaseService createSnowflake = new CreateDatabaseService().withName(DatabaseServiceResourceTest.getName(test, 1))
            .withServiceType(DatabaseServiceType.Snowflake).withJdbc(TestUtils.JDBC_INFO);
    DatabaseService service = DatabaseServiceResourceTest.createService(createSnowflake);
    SNOWFLAKE_REFERENCE = new EntityReference().withName(service.getName()).withId(service.getId())
            .withType(Entity.DATABASE_SERVICE);

    CreateDatabase create = DatabaseResourceTest.create(test).withService(SNOWFLAKE_REFERENCE);
    DATABASE = DatabaseResourceTest.createAndCheckDatabase(create);

    USER1 = UserResourceTest.createUser(UserResourceTest.create(test));
    USER_OWNER1 = new EntityReference().withId(USER1.getId()).withType("user");

    TEAM1 = TeamResourceTest.createTeam(TeamResourceTest.create(test));
    TEAM_OWNER1 = new EntityReference().withId(TEAM1.getId()).withType("team");
  }

  @Test
  public void post_tableWithLongName_400_badRequest(TestInfo test) {
    // Create table with mandatory name field empty
    CreateTable create = create(test).withName(TestUtils.LONG_ENTITY_NAME);
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> createTable(create));
    assertResponse(exception, BAD_REQUEST, "[name size must be between 1 and 64]");
  }

  @Test
  public void post_tableWithoutName_400_badRequest(TestInfo test) {
    // Create table with mandatory name field empty
    CreateTable create = create(test).withName("");
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> createTable(create));
    assertResponse(exception, BAD_REQUEST, "[name size must be between 1 and 64]");
  }

  @Test
  public void post_tableAlreadyExists_409_conflict(TestInfo test) throws HttpResponseException {
    CreateTable create = create(test);
    createTable(create);
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> createTable(create));
    assertResponse(exception, CONFLICT, CatalogExceptionMessage.ENTITY_ALREADY_EXISTS);
  }

  @Test
  public void post_validTables_200_OK(TestInfo test) throws HttpResponseException {
    // Create table with different optional fields
    // Optional field description
    CreateTable create = create(test).withDescription("description");
    createAndCheckTable(create);

    // Optional fields tableType
    create.withName(getTableName(test, 1)).withTableType(TableType.View);
    createAndCheckTable(create);
  }

  @Test
  public void post_tableWithUserOwner_200_ok(TestInfo test) throws HttpResponseException {
    createAndCheckTable(create(test).withOwner(USER_OWNER1));
  }

  @Test
  public void post_tableWithTeamOwner_200_ok(TestInfo test) throws HttpResponseException {
    createAndCheckTable(create(test).withOwner(TEAM_OWNER1));
  }

  @Test
  public void post_tableWithInvalidOwnerType_4xx(TestInfo test) {
    EntityReference owner = new EntityReference().withId(TEAM1.getId()); /* No owner type is set */
    CreateTable create = create(test).withOwner(owner);
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> createTable(create));
    TestUtils.assertResponseContains(exception, BAD_REQUEST, "type must not be null");
  }

  @Test
  public void post_tableWithInvalidDatabase_404(TestInfo test) {
    CreateTable create = create(test).withDatabase(TestUtils.NON_EXISTENT_ENTITY);
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> createTable(create));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound(Entity.DATABASE, TestUtils.NON_EXISTENT_ENTITY));
  }

  @Test
  public void post_tableWithNonExistentOwner_4xx(TestInfo test) {
    EntityReference owner = new EntityReference().withId(TestUtils.NON_EXISTENT_ENTITY).withType("user"); /* Random owner id is set */
    CreateTable create = create(test).withOwner(owner);
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> createTable(create));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound("User", TestUtils.NON_EXISTENT_ENTITY));
  }

  @Test
  public void put_tableUpdateWithNoChange_200(TestInfo test) throws HttpResponseException {
    CreateTable request = create(test).withOwner(USER_OWNER1);
    createAndCheckTable(request);

    // Update table two times successfully with PUT requests
    updateAndCheckTable(request, OK);
    updateAndCheckTable(request, OK);
  }

  @Test
  public void put_tableCreate_200(TestInfo test) throws HttpResponseException {
    // Create a new table with put
    CreateTable request = create(test).withOwner(USER_OWNER1);
    updateAndCheckTable(request.withName("newName").withDescription(null), CREATED);
  }

  @Test
  public void put_tableNullDescriptionUpdate_200(TestInfo test) throws HttpResponseException {
    // Create table with null description
    CreateTable request = create(test).withOwner(USER_OWNER1);
    createAndCheckTable(request);

    // Update null description with a new description
    Table table = updateAndCheckTable(request.withDescription("newDescription"), OK);
    assertEquals("newDescription", table.getDescription());
  }

  @Test
  public void put_tableEmptyDescriptionUpdate_200(TestInfo test) throws HttpResponseException {
    // Create table with empty description
    CreateTable request = create(test).withOwner(USER_OWNER1);
    createAndCheckTable(request);

    // Update empty description with a new description
    Table table = updateAndCheckTable(request.withDescription("newDescription"), OK);
    assertEquals("newDescription", table.getDescription());
  }

  @Test
  public void put_tableNonEmptyDescriptionUpdateIgnored_200(TestInfo test) throws HttpResponseException {
    CreateTable request = create(test).withOwner(USER_OWNER1).withDescription("description");
    createAndCheckTable(request);

    // Updating non-empty description is ignored
    Table table = updateTable(request.withDescription("newDescription"), OK);
    assertEquals("description", table.getDescription());
  }

  @Test
  public void put_tableOwnershipUpdate_200(TestInfo test) throws HttpResponseException {
    CreateTable request = create(test).withOwner(USER_OWNER1).withDescription("description");
    Table table = createAndCheckTable(request);
    checkOwnerOwns(USER_OWNER1, table.getId(), true);

    // Change ownership from USER_OWNER1 to TEAM_OWNER1
    updateAndCheckTable(request.withOwner(TEAM_OWNER1), OK);
    checkOwnerOwns(USER_OWNER1, table.getId(), false);
    checkOwnerOwns(TEAM_OWNER1, table.getId(), true);

    // Remove ownership
    table = updateAndCheckTable(request.withOwner(null), OK);
    assertNull(table.getOwner());
    checkOwnerOwns(TEAM_OWNER1, table.getId(), false);
  }

  @Test
  public void put_tableTableConstraintUpdate_200(TestInfo test) throws HttpResponseException {
    // Create table without table constraints
    CreateTable request = create(test).withOwner(USER_OWNER1).withDescription("description").withTableConstraints(null);
    Table table = createAndCheckTable(request);
    checkOwnerOwns(USER_OWNER1, table.getId(), true);

    // Update the table with constraints
    request = create(test).withOwner(USER_OWNER1).withDescription("description");
    table = updateAndCheckTable(request, OK);
  }

  @Test
  public void put_updateColumns_200(TestInfo test) throws HttpResponseException {
    int tagCategoryUsageCount = getTagCategoryUsageCount("user");
    int addressTagUsageCount = getTagUsageCount(USER_ADDRESS_TAG_LABEL.getTagFQN());
    int bankTagUsageCount = getTagUsageCount(USER_BANK_ACCOUNT_TAG_LABEL.getTagFQN());

    //
    // Create a table with column c1, type BIGINT, description c1 and tag USER_ADDRESS_TAB_LABEL
    //
    List<TagLabel> tags = new ArrayList<>(Arrays.asList(USER_ADDRESS_TAG_LABEL));
    List<Column> columns = singletonList(new Column().withName("c1").withColumnDataType(ColumnDataType.BIGINT)
            .withOrdinalPosition(1).withDescription("c1").withTags(tags));
    CreateTable request = create(test).withColumns(columns);
    Table table = createAndCheckTable(request);
    columns.get(0).setFullyQualifiedName(table.getFullyQualifiedName() + ".c1");

    // Ensure tag category and tag usage counts are updated
    assertEquals(tagCategoryUsageCount + 1, getTagCategoryUsageCount("user"));
    assertEquals(addressTagUsageCount + 1, getTagUsageCount(USER_ADDRESS_TAG_LABEL.getTagFQN()));
    assertEquals(bankTagUsageCount, getTagUsageCount(USER_BANK_ACCOUNT_TAG_LABEL.getTagFQN()));

    //
    // Update the c1 with additional tag USER_BANK_ACCOUNT_TAG_LABEL
    // Ensure description and previous tag is carried forward during update
    //
    tags.add(USER_BANK_ACCOUNT_TAG_LABEL);
    List<Column> updatedColumns = new ArrayList<>();
    updatedColumns.add(new Column().withName("c1").withColumnDataType(ColumnDataType.BIGINT).withTags(tags).withOrdinalPosition(1));
    table = updateAndCheckTable(request.withColumns(updatedColumns), OK);
    validateTags(columns.get(0).getTags(), table.getColumns().get(0).getTags());

    // Ensure tag usage counts are updated
    assertEquals(tagCategoryUsageCount + 2, getTagCategoryUsageCount("user"));
    assertEquals(addressTagUsageCount + 1, getTagUsageCount(USER_ADDRESS_TAG_LABEL.getTagFQN()));
    assertEquals(bankTagUsageCount + 1, getTagUsageCount(USER_BANK_ACCOUNT_TAG_LABEL.getTagFQN()));

    //
    // Add a new column and make sure it is added by PUT
    //
    updatedColumns.add(new Column().withName("c2").withColumnDataType(ColumnDataType.BINARY).withOrdinalPosition(2)
            .withFullyQualifiedName(table.getFullyQualifiedName() + ".c2").withTags(tags));
    table = updateAndCheckTable(request.withColumns(updatedColumns), OK);
    assertEquals(2, table.getColumns().size());
    validateTags(updatedColumns.get(0).getTags(), table.getColumns().get(0).getTags());
    validateTags(updatedColumns.get(1).getTags(), table.getColumns().get(1).getTags());

    // Ensure tag usage counts are updated - column c2 added both address and bank tags
    assertEquals(tagCategoryUsageCount + 4, getTagCategoryUsageCount("user"));
    assertEquals(addressTagUsageCount + 2, getTagUsageCount(USER_ADDRESS_TAG_LABEL.getTagFQN()));
    assertEquals(bankTagUsageCount + 2, getTagUsageCount(USER_BANK_ACCOUNT_TAG_LABEL.getTagFQN()));

    //
    // Remove a column c2 and make sure it is deleted by PUT
    //
    updatedColumns.remove(1);
    table = updateAndCheckTable(request.withColumns(updatedColumns), OK);
    assertEquals(1, table.getColumns().size());
    validateTags(columns.get(0).getTags(), table.getColumns().get(0).getTags());

    // Ensure tag usage counts are updated to reflect removal of column c2
    assertEquals(tagCategoryUsageCount + 2, getTagCategoryUsageCount("user"));
    assertEquals(addressTagUsageCount + 1, getTagUsageCount(USER_ADDRESS_TAG_LABEL.getTagFQN()));
    assertEquals(bankTagUsageCount + 1, getTagUsageCount(USER_BANK_ACCOUNT_TAG_LABEL.getTagFQN()));
  }

  @Test
  public void put_tableJoins_200(TestInfo test) throws HttpResponseException, ParseException {
    Table table1 = createAndCheckTable(create(test, 1));
    Table table2 = createAndCheckTable(create(test, 2));
    Table table3 = createAndCheckTable(create(test, 3));

    // Fully qualified names for table1, table2, table3 columns
    String t1c1 = table1.getFullyQualifiedName() + ".c1";
    String t1c2 = table1.getFullyQualifiedName() + ".c2";
    String t1c3 = table1.getFullyQualifiedName() + ".c3";
    String t2c1 = table2.getFullyQualifiedName() + ".c1";
    String t2c2 = table2.getFullyQualifiedName() + ".c2";
    String t2c3 = table2.getFullyQualifiedName() + ".c3";
    String t3c1 = table3.getFullyQualifiedName() + ".c1";
    String t3c2 = table3.getFullyQualifiedName() + ".c2";
    String t3c3 = table3.getFullyQualifiedName() + ".c3";

    List<ColumnJoin> reportedJoins = Arrays.asList(
            // table1.c1 is joined with table2.c1, and table3.c1 with join count 10
            new ColumnJoin().withColumnName("c1").withJoinedWith(Arrays.asList(
                    new JoinedWith().withFullyQualifiedName(t2c1).withJoinCount(10),
                    new JoinedWith().withFullyQualifiedName(t3c1).withJoinCount(10))),
            // table1.c2 is joined with table2.c1, and table3.c3 with join count 20
            new ColumnJoin().withColumnName("c2").withJoinedWith(Arrays.asList(
                    new JoinedWith().withFullyQualifiedName(t2c2).withJoinCount(20),
                    new JoinedWith().withFullyQualifiedName(t3c2).withJoinCount(20))),
            // table1.c3 is joined with table2.c1, and table3.c3 with join count 30
            new ColumnJoin().withColumnName("c3").withJoinedWith(Arrays.asList(
                    new JoinedWith().withFullyQualifiedName(t2c3).withJoinCount(30),
                    new JoinedWith().withFullyQualifiedName(t3c3).withJoinCount(30))));

    for (int i = 1; i <= 30; i++) {
      // Report joins starting from today back to 30 days. After every report, check the cumulative join count
      TableJoins table1Joins =
              new TableJoins().withDayCount(1).withStartDate(RestUtil.today(-(i-1))).withColumnJoins(reportedJoins);
      putJoins(table1.getId(), table1Joins);

      List<ColumnJoin> expectedJoins1 = Arrays.asList(
              // table1.c1 is joined with table2.c1, and table3.c1 with join count 10
              new ColumnJoin().withColumnName("c1").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t2c1).withJoinCount(10 * i),
                      new JoinedWith().withFullyQualifiedName(t3c1).withJoinCount(10 * i))),
              // table1.c2 is joined with table2.c1, and table3.c3 with join count 20
              new ColumnJoin().withColumnName("c2").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t2c2).withJoinCount(20 * i),
                      new JoinedWith().withFullyQualifiedName(t3c2).withJoinCount(20 * i))),
              // table1.c3 is joined with table2.c1, and table3.c3 with join count 30
              new ColumnJoin().withColumnName("c3").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t2c3).withJoinCount(30 * i),
                      new JoinedWith().withFullyQualifiedName(t3c3).withJoinCount(30 * i))));

      // getTable and ensure the following column joins are correct
      table1 = getTable(table1.getId(), "joins");
      validateColumnJoins(expectedJoins1, table1.getJoins());

      // getTable and ensure the following column joins are correct
      table2 = getTable(table2.getId(), "joins");
      List<ColumnJoin> expectedJoins2 = Arrays.asList(
              // table2.c1 is joined with table1.c1 with join count 10
              new ColumnJoin().withColumnName("c1").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t1c1).withJoinCount(10 * i))),
              // table2.c2 is joined with table1.c1 with join count 20
              new ColumnJoin().withColumnName("c2").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t1c2).withJoinCount(20 * i))),
              // table2.c3 is joined with table1.c1 with join count 30
              new ColumnJoin().withColumnName("c3").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t1c3).withJoinCount(30 * i))));
      TableJoins table2Joins = new TableJoins().withDayCount(1)
              .withStartDate(RestUtil.today(0)).withColumnJoins(expectedJoins2);
      validateColumnJoins(expectedJoins2, table2.getJoins());

      // getTable and ensure the following column joins
      table3 = getTable(table3.getId(), "joins");
      List<ColumnJoin> expectedJoins3 = Arrays.asList(
              // table3.c1 is joined with table1.c1 with join count 10
              new ColumnJoin().withColumnName("c1").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t1c1).withJoinCount(10 * i))),
              // table3.c2 is joined with table1.c1 with join count 20
              new ColumnJoin().withColumnName("c2").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t1c2).withJoinCount(20 * i))),
              // table3.c3 is joined with table1.c1 with join count 30
              new ColumnJoin().withColumnName("c3").withJoinedWith(Arrays.asList(
                      new JoinedWith().withFullyQualifiedName(t1c3).withJoinCount(30 * i))));
      TableJoins table3Joins = new TableJoins().withDayCount(1)
              .withStartDate(RestUtil.today(0)).withColumnJoins(expectedJoins3);
      validateColumnJoins(expectedJoins3, table3.getJoins());

      // Report again for the previous day and make sure aggregate counts are correct
      table1Joins = new TableJoins().withDayCount(1).withStartDate(RestUtil.today(-1)).withColumnJoins(reportedJoins);
      putJoins(table1.getId(), table1Joins);
      table1 = getTable(table1.getId(), "joins");
    }
  }

  @Test
  public void put_tableJoinsInvalidColumnName_4xx(TestInfo test) throws HttpResponseException, ParseException {
    Table table1 = createAndCheckTable(create(test, 1));
    Table table2 = createAndCheckTable(create(test, 2));

    List<ColumnJoin> joins = singletonList(new ColumnJoin().withColumnName("c1"));
    TableJoins tableJoins = new TableJoins().withStartDate(RestUtil.today(0))
            .withDayCount(1).withColumnJoins(joins);

    // Invalid database name
    String columnFQN = "invalidDB";
    JoinedWith joinedWith = new JoinedWith().withFullyQualifiedName(columnFQN);
    joins.get(0).withJoinedWith(singletonList(joinedWith));
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> putJoins(table1.getId(), tableJoins));
    assertResponse(exception, BAD_REQUEST, CatalogExceptionMessage.invalidColumnFQN(columnFQN));

    // Invalid table name
    columnFQN = table2.getDatabase().getName() + ".invalidTable";
    joinedWith = new JoinedWith().withFullyQualifiedName(columnFQN);
    joins.get(0).withJoinedWith(singletonList(joinedWith));
    exception = assertThrows(HttpResponseException.class, () -> putJoins(table1.getId(), tableJoins));
    assertResponse(exception, BAD_REQUEST, CatalogExceptionMessage.invalidColumnFQN(columnFQN));

    // Invalid column name
    columnFQN = table2.getFullyQualifiedName() + ".invalidColumn";
    joinedWith = new JoinedWith().withFullyQualifiedName(columnFQN);
    joins.get(0).withJoinedWith(singletonList(joinedWith));
    exception = assertThrows(HttpResponseException.class, () -> putJoins(table1.getId(), tableJoins));
    assertResponse(exception, BAD_REQUEST, CatalogExceptionMessage.invalidColumnFQN(columnFQN));

    // Invalid date older than 30 days
    joinedWith = new JoinedWith().withFullyQualifiedName(table2.getFullyQualifiedName() + ".c1");
    joins.get(0).withJoinedWith(singletonList(joinedWith));
    tableJoins.withStartDate(RestUtil.today(-30));  // 30 days older than today
    exception = assertThrows(HttpResponseException.class, () -> putJoins(table1.getId(), tableJoins));
    assertResponse(exception, BAD_REQUEST, "Date range can only include past 30 days starting today");
  }

  public void validateColumnJoins(List<ColumnJoin> expected, TableJoins actual) throws ParseException {
    // Table reports last 30 days of aggregated join count
    assertEquals(actual.getStartDate(), CommonUtil.getDateStringByOffset(DATE_FORMAT, RestUtil.today(0), -30));
    assertEquals(actual.getDayCount(), 30);

    // Sort the columnJoins and the joinedWith to account for different ordering
    expected.sort(new ColumnJoinComparator());
    expected.forEach(c -> c.getJoinedWith().sort(new JoinedWithComparator()));
    actual.getColumnJoins().sort(new ColumnJoinComparator());
    actual.getColumnJoins().forEach(c -> c.getJoinedWith().sort(new JoinedWithComparator()));
    assertEquals(expected, actual.getColumnJoins());
  }

  public static class ColumnJoinComparator implements Comparator<ColumnJoin> {
    @Override
    public int compare(ColumnJoin columnJoin, ColumnJoin t1) {
      return columnJoin.getColumnName().compareTo(t1.getColumnName());
    }
  }

  public static class JoinedWithComparator implements Comparator<JoinedWith> {
    @Override
    public int compare(JoinedWith joinedWith, JoinedWith t1) {
      return joinedWith.getFullyQualifiedName().compareTo(t1.getFullyQualifiedName());
    }
  }

  public void validateColumnJoins(List<ColumnJoin> columnJoins, String[][] expectedColumnJoins) {
    assertEquals(3, columnJoins.size()); // Total number of columns that have joins is 3
    for (String[] expectedColumnJoin : expectedColumnJoins) {
      for (ColumnJoin columnJoin : columnJoins) {
        assertEquals(expectedColumnJoin.length - 1, columnJoin.getJoinedWith().size());
        if (expectedColumnJoin[0].equals(columnJoin.getColumnName())) {
          for (int i = 1; i < expectedColumnJoin.length; i++) {
            assertTrue(columnJoin.getJoinedWith().contains(expectedColumnJoin[i]));
          }
        }
      }
    }
  }

  @Test
  public void put_tableSampleData_200(TestInfo test) throws HttpResponseException {
    Table table = createAndCheckTable(create(test));
    List<String> columns = Arrays.asList("c1", "c2", "c3");

    // Add 3 rows of sample data for 3 columns
    List<List<Object>> rows = Arrays.asList(Arrays.asList("c1Value1", 1, true),
                                            Arrays.asList("c1Value2", null, false),
                                            Arrays.asList("c1Value3", 3, true));

    TableData tableData = new TableData().withColumns(columns).withRows(rows);
    putSampleData(table.getId(), tableData);

    table = getTable(table.getId(), "sampleData");
    assertEquals(tableData, table.getSampleData());
  }

  @Test
  public void put_tableInvalidSampleData_4xx(TestInfo test) throws HttpResponseException {
    Table table = createAndCheckTable(create(test));
    TableData tableData = new TableData();

    // Send sample data with invalid column name
    List<String> columns = Arrays.asList("c1", "c2", "invalidColumn");  // Invalid column name
    List<List<Object>> rows = singletonList(Arrays.asList("c1Value1", 1, true)); // Valid sample data
    tableData.withColumns(columns).withRows(rows);
    HttpResponseException exception = assertThrows(HttpResponseException.class, ()
            -> putSampleData(table.getId(), tableData));
    TestUtils.assertResponseContains(exception, BAD_REQUEST, "Invalid column name invalidColumn");

    // Send sample data that has more samples than the number of columns
    columns = Arrays.asList("c1", "c2", "c3");  // Invalid column name
    rows = singletonList(Arrays.asList("c1Value1", 1, true, "extra value")); // Extra value
    tableData.withColumns(columns).withRows(rows);
    exception = assertThrows(HttpResponseException.class, () -> putSampleData(table.getId(), tableData));
    TestUtils.assertResponseContains(exception, BAD_REQUEST, "Number of columns is 3 but row has 4 sample values");

    // Send sample data that has less samples than the number of columns
    columns = Arrays.asList("c1", "c2", "c3");  // Invalid column name
    rows = singletonList(Arrays.asList("c1Value1", 1 /* Missing Value */));
    tableData.withColumns(columns).withRows(rows);
    exception = assertThrows(HttpResponseException.class, () -> putSampleData(table.getId(), tableData));
    TestUtils.assertResponseContains(exception, BAD_REQUEST, "Number of columns is 3 but row has 2 sample values");
  }

  @Test
  public void get_nonExistentTable_404_notFound() {
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> getTable(TestUtils.NON_EXISTENT_ENTITY));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound(Entity.TABLE, TestUtils.NON_EXISTENT_ENTITY));
  }

  @Test
  public void get_tableWithDifferentFields_200_OK(TestInfo test) throws HttpResponseException {
    CreateTable create = create(test).withDescription("description").withOwner(USER_OWNER1);
    Table table = createAndCheckTable(create);
    validateGetWithDifferentFields(table, false);
  }

  @Test
  public void get_tableByNameWithDifferentFields_200_OK(TestInfo test) throws HttpResponseException {
    CreateTable create = create(test).withDescription("description").withOwner(USER_OWNER1);
    Table table = createAndCheckTable(create);
    validateGetWithDifferentFields(table, true);
  }

  @Test
  @Order(1) // Run this test first as other tables created in other tests will interfere with listing
  public void get_tableListWithDifferentFields_200_OK(TestInfo test) throws HttpResponseException {
    CreateTable create = create(test, 1).withDescription("description").withOwner(USER_OWNER1)
            .withTags(singletonList(USER_ADDRESS_TAG_LABEL));
    createAndCheckTable(create);
    CreateTable create1 = create(test, 2).withDescription("description").withOwner(USER_OWNER1);
    createAndCheckTable(create1);

    // Check tag category and tag usage counts
    assertEquals(7, getTagCategoryUsageCount("user")); // 1 table tags + 3*2 column tags from COLUMNS
    assertEquals(5, getTagUsageCount(USER_ADDRESS_TAG_LABEL.getTagFQN())); // 1 table tag and 2*2 column tags
    assertEquals(2, getTagUsageCount(USER_BANK_ACCOUNT_TAG_LABEL.getTagFQN())); // 2*1 column tags

    TableList tableList = listTables(null, null); // List tables
    assertEquals(2, tableList.getData().size());
    assertFields(tableList.getData(), null);

    TableList tableList1 = listTables(null, DATABASE.getFullyQualifiedName()); // List tables with databaseFQN as filter
    assertEquals(tableList.getData().size(), tableList1.getData().size());
    assertFields(tableList1.getData(), null);

    // GET .../tables?fields=columns,tableConstraints
    String fields = "columns,tableConstraints";
    tableList = listTables(fields, null);
    assertEquals(2, tableList.getData().size());
    assertFields(tableList.getData(), fields);

    // List tables with databaseFQN as filter
    tableList1 = listTables(fields, DATABASE.getFullyQualifiedName());
    assertEquals(tableList.getData().size(), tableList1.getData().size());
    assertFields(tableList1.getData(), fields);

    // GET .../tables?fields=usageSummary,owner,service
    fields = "usageSummary,owner,database";
    tableList = listTables( fields, null);
    assertEquals(2, tableList.getData().size());
    assertFields(tableList.getData(), fields);
    for (Table table : tableList.getData()) {
      assertEquals(table.getOwner().getId(), USER_OWNER1.getId());
      assertEquals(table.getOwner().getType(), USER_OWNER1.getType());
      assertEquals(table.getDatabase().getId(), DATABASE.getId());
      assertEquals(table.getDatabase().getName(), DATABASE.getName());
    }

    // List tables with databaseFQN as filter
    tableList1 = listTables(fields, DATABASE.getFullyQualifiedName());
    assertEquals(tableList.getData().size(), tableList1.getData().size());
    assertFields(tableList1.getData(), fields);
  }

  @Test
  public void get_tableListWithInvalidLimit_4xx() {
    // Limit must be >= 1 and <= 1000,000
    HttpResponseException exception = assertThrows(HttpResponseException.class, ()
            -> listTables(null, null, -1, null, null));
    assertResponse(exception, BAD_REQUEST, "[query param limit must be greater than or equal to 1]");

    exception = assertThrows(HttpResponseException.class, ()
            -> listTables(null, null, 0, null, null));
    assertResponse(exception, BAD_REQUEST, "[query param limit must be greater than or equal to 1]");

    exception = assertThrows(HttpResponseException.class, ()
            -> listTables(null, null, 1000001, null, null));
    assertResponse(exception, BAD_REQUEST, "[query param limit must be less than or equal to 1000000]");
  }

  @Test
  public void get_tableListWithInvalidPaginationCursors_4xx() {
    // Passing both before and after cursors is invalid
    HttpResponseException exception = assertThrows(HttpResponseException.class, ()
            -> listTables(null, null, 1, "", ""));
    assertResponse(exception, BAD_REQUEST, "Only one of before or after query parameter allowed");
  }

  /**
   * For cursor based pagination and implementation details:
   * @see org.openmetadata.catalog.util.ResultList#ResultList(List, int, String, String)
   *
   * The tests and various CASES referenced are base on that.
   */
  @Test
  public void get_tableListWithPagination_200(TestInfo test) throws HttpResponseException {
    // Create a large number of tables
    int maxTables = 40;
    for (int i = 0; i < maxTables; i++) {
      createTable(create(test, i));
    }

    // List all tables and use it for checking pagination
    TableList allTables = listTables(null, null, 1000000, null, null);
    int totalRecords = allTables.getData().size();
    printTables(allTables);

    // List tables with limit set from 1 to maxTables size
    // Each time comapare the returned list with allTables list to make sure right results are returned
    for (int limit = 1; limit < maxTables; limit++) {
      String after = null;
      String before = null;
      int pageCount = 0;
      int indexInAllTables = 0;
      TableList forwardPage;
      TableList backwardPage;
      do { // For each limit (or page size) - forward scroll till the end
        LOG.info("Limit {} forward scrollCount {} afterCursor {}", limit, pageCount, after);
        forwardPage = listTables(null, null, limit, null, after);
        after = forwardPage.getPaging().getAfter();
        before = forwardPage.getPaging().getBefore();
        assertEntityPagination(allTables.getData(), forwardPage, limit, indexInAllTables);

        if (pageCount == 0) {  // CASE 0 - First page is being returned. There is no before cursor
          assertNull(before);
        } else {
          // Make sure scrolling back based on before cursor returns the correct result
          backwardPage = listTables(null, null, limit, before, null);
          assertEntityPagination(allTables.getData(), backwardPage, limit, (indexInAllTables - limit));
        }

        printTables(forwardPage);
        indexInAllTables += forwardPage.getData().size();
        pageCount++;
      } while (after != null);

      // We have now reached the last page - test backward scroll till the beginning
      pageCount = 0;
      indexInAllTables = totalRecords - limit - forwardPage.getData().size() ;
      do {
        LOG.info("Limit {} backward scrollCount {} beforeCursor {}", limit, pageCount, before);
        forwardPage = listTables(null, null, limit, before, null);
        printTables(forwardPage);
        before = forwardPage.getPaging().getBefore();
        assertEntityPagination(allTables.getData(), forwardPage, limit, indexInAllTables);
        pageCount++;
        indexInAllTables -= forwardPage.getData().size();
      } while (before != null);
    }
  }

  private void printTables(TableList list) {
    list.getData().forEach(table -> LOG.info("Table {}", table.getFullyQualifiedName()));
    LOG.info("before {} after {} ", list.getPaging().getBefore(), list.getPaging().getAfter());
  }

  @Test
  public void delete_table_200_ok(TestInfo test) throws HttpResponseException {
    Table table = createTable(create(test));
    deleteTable(table.getId());
  }

  @Test
  public void delete_nonExistentTable_404() {
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> getTable(TestUtils.NON_EXISTENT_ENTITY));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound(Entity.TABLE, TestUtils.NON_EXISTENT_ENTITY));
  }

  @Test
  public void patch_tableAttributes_200_ok(TestInfo test) throws HttpResponseException, JsonProcessingException {
    // Create table without description, table tags, tier, owner, tableType
    Table table = createTable(create(test)).withTableConstraints(null);
    assertNull(table.getDescription());
    assertNull(table.getOwner());
    assertNull(table.getTableType());
    assertNull(table.getTableConstraints());

    // Add description, table tags, tier, owner, tableType, and tableContraints when previously they were null
    List<TableConstraint> tableConstraints = List.of(new TableConstraint().withConstraintType(ConstraintType.UNIQUE)
            .withColumns(List.of(COLUMNS.get(0).getName())));
    List<TagLabel> tableTags = singletonList(USER_ADDRESS_TAG_LABEL);
    table = patchTableAttributesAndCheck(table, "description", TEAM_OWNER1, TableType.Regular, tableConstraints,
            tableTags);
    table.setOwner(TEAM_OWNER1); // Get rid of href and name returned in the response for owner

    // Replace description, tier, owner, tableType, tableConstraints
    tableConstraints = List.of(new TableConstraint().withConstraintType(ConstraintType.UNIQUE)
            .withColumns(List.of(COLUMNS.get(1).getName())));
    tableTags = singletonList(USER_BANK_ACCOUNT_TAG_LABEL);
    table = patchTableAttributesAndCheck(table, "description1", USER_OWNER1, TableType.External, tableConstraints,
            tableTags);
    table.setOwner(USER_OWNER1); // Get rid of href and name returned in the response for owner

    // Remove description, tier, owner, tableType, tableConstraints
    patchTableAttributesAndCheck(table, null, null, null, null, null);
  }

  @Test
  public void patch_tableIDChange_400(TestInfo test) throws HttpResponseException, JsonProcessingException {
    // Ensure table ID can't be changed using patch
    Table table = createTable(create(test));
    UUID oldTableId = table.getId();
    String tableJson = JsonUtils.pojoToJson(table);
    table.setId(UUID.randomUUID());
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> patchTable(oldTableId, tableJson, table));
    assertResponse(exception, BAD_REQUEST, CatalogExceptionMessage.readOnlyAttribute(Entity.TABLE, "id"));
  }

  @Test
  public void patch_tableNameChange_400(TestInfo test) throws HttpResponseException, JsonProcessingException {
    // Ensure table name can't be changed using patch
    Table table = createTable(create(test));
    String tableJson = JsonUtils.pojoToJson(table);
    table.setName("newName");
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> patchTable(tableJson, table));
    assertResponse(exception, BAD_REQUEST, CatalogExceptionMessage.readOnlyAttribute(Entity.TABLE, "name"));
  }

  @Test
  public void patch_tableRemoveDatabase_400(TestInfo test) throws HttpResponseException, JsonProcessingException {
    // Ensure table database it belongs to can't be removed
    Table table = createTable(create(test).withDatabase(DATABASE.getId()));
    String tableJson = JsonUtils.pojoToJson(table);
    table.setDatabase(null);
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> patchTable(tableJson, table));
    assertResponse(exception, BAD_REQUEST, "Table relationship database can't be removed");
  }

  @Test
  public void patch_tableReplaceDatabase_400(TestInfo test) throws HttpResponseException, JsonProcessingException {
    // Ensure table database it belongs to can't be removed
    Table table = createTable(create(test).withDatabase(DATABASE.getId()));
    String tableJson = JsonUtils.pojoToJson(table);
    table.getDatabase().setId(UUID.randomUUID());
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> patchTable(tableJson, table));
    assertResponse(exception, BAD_REQUEST, "Table relationship database can't be replaced");
  }

  @Test
  public void put_addDeleteFollower_200(TestInfo test) throws HttpResponseException {
    Table table = createAndCheckTable(create(test));

    // Add follower to the table
    User user1 = UserResourceTest.createUser(UserResourceTest.create(test, 1));
    addAndCheckFollower(table, user1.getId(), CREATED, 1);

    // Add the same user as follower and make sure no errors are thrown and return response is OK (and not CREATED)
    addAndCheckFollower(table, user1.getId(), OK, 1);

    // Add a new follower to the table
    User user2 = UserResourceTest.createUser(UserResourceTest.create(test, 2));
    addAndCheckFollower(table, user2.getId(), CREATED, 2);

    // Delete followers and make sure they are deleted
    deleteAndCheckFollower(table, user1.getId(), 1);
    deleteAndCheckFollower(table, user2.getId(), 0);
  }

  @Test
  public void put_addDeleteInvalidFollower_200(TestInfo test) throws HttpResponseException {
    Table table = createAndCheckTable(create(test));

    // Add non existent user as follower to the table
    HttpResponseException exception = assertThrows(HttpResponseException.class, () ->
            addAndCheckFollower(table, TestUtils.NON_EXISTENT_ENTITY, CREATED, 1));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound("User", TestUtils.NON_EXISTENT_ENTITY));

    // Delete non existent user as follower to the table
    exception = assertThrows(HttpResponseException.class, () ->
            deleteAndCheckFollower(table, TestUtils.NON_EXISTENT_ENTITY, 1));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound("User", TestUtils.NON_EXISTENT_ENTITY));
  }

  private Table patchTableAttributesAndCheck(Table table, String description, EntityReference owner,
                                             TableType tableType, List<TableConstraint> tableConstraints,
                                             List<TagLabel> tags)
          throws JsonProcessingException, HttpResponseException {
    String tableJson = JsonUtils.pojoToJson(table);

    // Update the table attributes
    table.setDescription(description);
    table.setOwner(owner);
    table.setTableType(tableType);
    table.setTableConstraints(tableConstraints);
    table.setTags(tags);

    // Validate information returned in patch response has the updates
    Table updatedTable = patchTable(tableJson, table);
    validateTable(updatedTable, table.getDescription(), owner, null, tableType, tableConstraints, tags);

    // GET the table and Validate information returned
    Table getTable = getTable(table.getId(), "owner,tableConstraints,tags");
    validateTable(getTable, table.getDescription(), owner, null, tableType, tableConstraints, tags);
    return updatedTable;
  }

  // TODO disallow changing href, usage
  // TODO allow changing columns, tableConstraints
  // TODO Change column attributes
  // TODO Add column
  // TODO Remove column
  public static Table createAndCheckTable(CreateTable create) throws HttpResponseException {
    // Validate table created has all the information set in create request
    Table table = createTable(create);
    validateTable(table, create.getDescription(), create.getOwner(),
            create.getDatabase(), create.getTableType(), create.getTableConstraints(), create.getTags());
    validateTags(create.getTags(), table.getTags());

    // GET table created and ensure it has all the information set in create request
    Table getTable = getTable(table.getId(), "owner,database,tags,tableConstraints");
    validateTable(getTable, create.getDescription(), create.getOwner(),
            create.getDatabase(), create.getTableType(), create.getTableConstraints(), create.getTags());

    // If owner information is set, GET and make sure the user or team has the table in owns list
    checkOwnerOwns(create.getOwner(), table.getId(), true);
    return table;
  }

  void assertFields(List<Table> tableList, String fieldsParam) {
    tableList.forEach(t -> assertFields(t, fieldsParam));
  }

  void assertFields(Table table, String fieldsParam) {
    Fields fields = new Fields(TableResource.FIELD_LIST, fieldsParam);

    if (fields.contains("usageSummary")) {assertNotNull(table.getUsageSummary());} else {
      assertNull(table.getUsageSummary());
    }
    if (fields.contains("owner")) {assertNotNull(table.getOwner());} else {
      assertNull(table.getOwner());
    }
    if (fields.contains("columns")) {
      assertNotNull(table.getColumns());
      if (fields.contains("tags")) {
        table.getColumns().forEach(column -> assertNotNull(column.getTags()));
      } else {
        table.getColumns().forEach(column -> assertNull(column.getTags()));
      }
    } else {
      assertNull(table.getColumns());
    }
    if (fields.contains("tableConstraints")) {assertNotNull(table.getTableConstraints());} else {
      assertNull(table.getTableConstraints());
    }
    if (fields.contains("database")) {assertNotNull(table.getDatabase());} else {
      assertNull(table.getDatabase());
    }
    if (fields.contains("tags")) {
      assertNotNull(table.getTags());
    } else {
      assertNull(table.getTags());
    }
  }

  /** Validate returned fields GET .../tables/{id}?fields="..." or GET .../tables/name/{fqn}?fields="..." */
  private void validateGetWithDifferentFields(Table table, boolean byName) throws HttpResponseException {
    // GET .../tables/{id}
    table = byName ? getTableByName(table.getFullyQualifiedName(), null) : getTable(table.getId());
    assertFields(table, null);

    // GET .../tables/{id}?fields=columns,tableConstraints
    String fields = "columns,tableConstraints";
    table = byName ? getTableByName(table.getFullyQualifiedName(), fields) : getTable(table.getId(), fields);
    assertFields(table, fields);

    // GET .../tables/{id}?fields=columns,usageSummary,owner,database,tags
    fields = "columns,usageSummary,owner,database,tags";
    table = byName ? getTableByName(table.getFullyQualifiedName(), fields) : getTable(table.getId(), fields);
    assertEquals(table.getOwner().getId(), USER_OWNER1.getId());
    assertEquals(table.getOwner().getType(), USER_OWNER1.getType());
    assertEquals(table.getDatabase().getId(), DATABASE.getId());
    assertEquals(table.getDatabase().getName(), DATABASE.getName());
  }

  private static void validateTags(List<TagLabel> expectedList, List<TagLabel> actualList) throws HttpResponseException {
    if (expectedList == null) {
      return;
    }
    assertTrue(actualList.containsAll(expectedList));

    // Add derived tags to the expected list
    // Make sure both expected tags and derived exist
    for (TagLabel expected : expectedList) {
      List<TagLabel> derived = EntityUtil.getDerivedTags(expected, TagResourceTest.getTag(expected.getTagFQN()));
      assertTrue(actualList.containsAll(derived));
    }
  }

  public static Table createTable(CreateTable create) throws HttpResponseException {
    return TestUtils.post(CatalogApplicationTest.getResource("tables"), create, Table.class);
  }

  private static void validateTable(Table table, String expectedDescription, EntityReference expectedOwner,
                                    UUID expectedDatabaseId, TableType expectedTableType,
                                    List<TableConstraint> expectedTableConstraints, List<TagLabel> expectedTags) throws HttpResponseException {
    assertNotNull(table.getId());
    assertNotNull(table.getHref());
    assertNotNull(table.getFullyQualifiedName());
    assertEquals(expectedDescription, table.getDescription());
    assertEquals(expectedTableType, table.getTableType());

    // Validate owner
    if (expectedOwner != null) {
      TestUtils.validateEntityReference(table.getOwner());
      assertEquals(expectedOwner.getId(), table.getOwner().getId());
      assertEquals(expectedOwner.getType(), table.getOwner().getType());
      assertNotNull(table.getOwner().getHref());
    }

    // Validate database
    if (expectedDatabaseId != null) {
      TestUtils.validateEntityReference(table.getDatabase());
      assertEquals(expectedDatabaseId, table.getDatabase().getId());
    }

    // Validate table contraints
    assertEquals(expectedTableConstraints, table.getTableConstraints());
    validateTags(expectedTags, table.getTags());
    TestUtils.validateEntityReference(table.getFollowers());
  }

  public static Table getTable(UUID id) throws HttpResponseException {
    return getTable(id, null);
  }

  public static Table getTable(UUID id, String fields) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource("tables/" + id);
    target = fields != null ? target.queryParam("fields", fields) : target;
    return TestUtils.get(target, Table.class);
  }

  public static Table getTableByName(String fqn, String fields) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource("tables/name/" + fqn);
    target = fields != null ? target.queryParam("fields", fields) : target;
    return TestUtils.get(target, Table.class);
  }

  public static TableList listTables(String fields, String databaseParam) throws HttpResponseException {
    return listTables(fields, databaseParam, null, null, null);
  }

  public static TableList listTables(String fields, String databaseParam, Integer limit, String before, String after) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource("tables");
    target = fields != null ? target.queryParam("fields", fields) : target;
    target = databaseParam != null ? target.queryParam("database", databaseParam) : target;
    target = limit != null ? target.queryParam("limit", limit) : target;
    target = before != null ? target.queryParam("before", before) : target;
    target = after != null ? target.queryParam("after", after) : target;
    return TestUtils.get(target, TableList.class);
  }

  public static CreateTable create(TestInfo test) {
    TableConstraint constraint = new TableConstraint().withConstraintType(ConstraintType.UNIQUE)
            .withColumns(List.of(COLUMNS.get(0).getName()));
    return new CreateTable().withName(getTableName(test)).withDatabase(DATABASE.getId()).withColumns(COLUMNS)
            .withTableConstraints(List.of(constraint));
  }

  public static CreateTable create(TestInfo test, int index) {
    TableConstraint constraint = new TableConstraint().withConstraintType(ConstraintType.UNIQUE)
            .withColumns(List.of(COLUMNS.get(0).getName()));
    return new CreateTable().withName(getTableName(test, index)).withDatabase(DATABASE.getId()).withColumns(COLUMNS)
            .withTableConstraints(List.of(constraint));
  }

  /**
   * A method variant to be called form other tests to create a table without depending on Database, DatabaseService
   * set up in the {@code setup()} method
   */
  public static Table createTable(TestInfo test, int index) throws HttpResponseException {
    DatabaseService service = DatabaseServiceResourceTest.createService(DatabaseServiceResourceTest.create(test));
    EntityReference serviceRef =
            new EntityReference().withName(service.getName()).withId(service.getId()).withType(Entity.DATABASE_SERVICE);
    Database database =
            DatabaseResourceTest.createAndCheckDatabase(DatabaseResourceTest.create(test).withService(serviceRef));
    CreateTable create =
            new CreateTable().withName(getTableName(test, index)).withDatabase(database.getId()).withColumns(COLUMNS);
    return createTable(create);
  }

  public static Table updateAndCheckTable(CreateTable create, Status status) throws HttpResponseException {
    Table updatedTable = updateTable(create, status);
    validateTable(updatedTable, create.getDescription(), create.getOwner(), create.getDatabase(),
            create.getTableType(), create.getTableConstraints(), create.getTags());

    // GET the newly updated database and validate
    Table getTable = getTable(updatedTable.getId(), "database,owner,tableConstraints,tags");
    validateTable(getTable, create.getDescription(), create.getOwner(), create.getDatabase(), create.getTableType(),
            create.getTableConstraints(), create.getTags());
    // TODO columns check
    return updatedTable;
  }

  public static Table updateTable(CreateTable create, Status status) throws HttpResponseException {
    return TestUtils.put(CatalogApplicationTest.getResource("tables"), create, Table.class, status);
  }

  public static void putJoins(UUID tableId, TableJoins joins) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource("tables/" + tableId + "/joins");
    TestUtils.put(target, joins, OK);
  }

  public static void putSampleData(UUID tableId, TableData data) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource("tables/" + tableId + "/sampleData");
    TestUtils.put(target, data, OK);
  }

  private void deleteTable(UUID id) throws HttpResponseException {
    TestUtils.delete(CatalogApplicationTest.getResource("tables/" + id));

    // Check to make sure database does not exist
    HttpResponseException exception = assertThrows(HttpResponseException.class, () -> getTable(id));
    assertResponse(exception, NOT_FOUND, CatalogExceptionMessage.entityNotFound(Entity.TABLE, id));
  }

  private Table patchTable(UUID tableId, String originalJson, Table updatedTable) throws JsonProcessingException, HttpResponseException {
    String updateTableJson = JsonUtils.pojoToJson(updatedTable);
    JsonPatch patch = JsonSchemaUtil.getJsonPatch(originalJson, updateTableJson);
    return TestUtils.patch(CatalogApplicationTest.getResource("tables/" + tableId), patch, Table.class);
  }

  private Table patchTable(String originalJson, Table updatedTable) throws JsonProcessingException, HttpResponseException {
    return patchTable(updatedTable.getId(), originalJson, updatedTable);
  }

  public static void addAndCheckFollower(Table table, UUID userId, Status status, int totalFollowerCount) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource(String.format("tables/%s/followers", table.getId()));
    TestUtils.put(target, userId.toString(), status);

    // GET .../tables/{tableId} returns newly added follower
    Table getTable = getTable(table.getId(), "followers");
    assertEquals(totalFollowerCount, getTable.getFollowers().size());
    TestUtils.validateEntityReference(getTable.getFollowers());
    boolean followerFound = false;
    for (EntityReference followers : getTable.getFollowers()) {
      if (followers.getId().equals(userId)) {
        followerFound = true;
        break;
      }
    }
    assertTrue(followerFound, "Follower added was not found in table get response");

    // GET .../users/{userId} shows user as following table
    checkUserFollowing(userId, table.getId(), true);
  }

  private void deleteAndCheckFollower(Table table, UUID userId, int totalFollowerCount) throws HttpResponseException {
    WebTarget target = CatalogApplicationTest.getResource(String.format("tables/%s/followers/%s", table.getId(), userId));
    TestUtils.delete(target);

    Table getTable = checkFollowerDeleted(table.getId(), userId);
    assertEquals(totalFollowerCount, getTable.getFollowers().size());
  }

  public static Table checkFollowerDeleted(UUID tableId, UUID userId) throws HttpResponseException {
    Table getTable = getTable(tableId, "followers");
    TestUtils.validateEntityReference(getTable.getFollowers());
    boolean followerFound = false;
    for (EntityReference followers : getTable.getFollowers()) {
      if (followers.getId().equals(userId)) {
        followerFound = true;
        break;
      }
    }
    assertFalse(followerFound, "Follower deleted is still found in table get response");

    // GET .../users/{userId} shows user as following table
    checkUserFollowing(userId, tableId, false);
    return getTable;
  }

  private static void checkOwnerOwns(EntityReference owner, UUID tableId, boolean expectedOwning) throws HttpResponseException {
    if (owner != null) {
      UUID ownerId = owner.getId();
      List<EntityReference> ownsList;
      if (owner.getType().equals(Entity.USER)) {
        User user = UserResourceTest.getUser(ownerId, "owns");
        ownsList = user.getOwns();
      } else if (owner.getType().equals(Entity.TEAM)) {
        Team team = TeamResourceTest.getTeam(ownerId, "owns");
        ownsList = team.getOwns();
      } else {
        throw new IllegalArgumentException("Invalid owner type " + owner.getType());
      }

      boolean owning = false;
      for (EntityReference owns : ownsList) {
        TestUtils.validateEntityReference(owns);
        if (owns.getId().equals(tableId)) {
          owning = true;
          break;
        }
      }
      assertEquals(expectedOwning, owning, "Ownership not correct in the owns list for " + owner.getType());
    }
  }

  private static void checkUserFollowing(UUID userId, UUID tableId, boolean expectedFollowing) throws HttpResponseException {
    // GET .../users/{userId} shows user as following table
    boolean following = false;
    User user = UserResourceTest.getUser(userId, "follows");
    for (EntityReference follows : user.getFollows()) {
      TestUtils.validateEntityReference(follows);
      if (follows.getId().equals(tableId)) {
        following = true;
        break;
      }
    }
    assertEquals(expectedFollowing, following, "Follower list for the user is invalid");
  }

  private static int getTagUsageCount(String tagFQN) throws HttpResponseException {
    return TagResourceTest.getTag(tagFQN, "usageCount").getUsageCount();
  }

  private static int getTagCategoryUsageCount(String name) throws HttpResponseException {
    return TagResourceTest.getCategory(name, "usageCount").getUsageCount();
  }

  public static String getTableName(TestInfo test) {
    return String.format("table_%s", test.getDisplayName());
  }

  public static String getTableName(TestInfo test, int index) {
    return String.format("table%d_%s", index, test.getDisplayName());
  }
}
