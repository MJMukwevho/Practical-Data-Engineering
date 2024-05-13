import sys
import pytest
import psycopg2

sys.path.insert(0, "custom_lib.zip")
from custom_lib.sql_base import sql_base


@pytest.fixture
def create_database_conn():
    db = sql_base()

    db.create_schema("test_schema")

    db.create_table(
        schema_name="test_schema",
        table_name="test_table",
        table_definitions="name text, surname text, age integer",
    )


def test_check_test_schema_exists(create_database_conn):
    # Use the existing database connection obtained from the fixture
    db = sql_base()

    # Execute the query using the database connection
    query = f'SELECT * FROM "test_schema".test_table'
    response = db.sql_runner(query)

    # If the response [], the schema exists
    assert response == []
