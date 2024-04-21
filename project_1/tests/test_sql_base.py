import pytest
from src.sql_base import sql_base


class test_sql_base:

    def setup(self):

        self.database = sql_base()

    def run(self):
        self.test_schema_creation()
        self.test_table_create()

    def test_schema_creation(self):

        schema_name = "test_schema"
        self.database.create_schema(schema_name=schema_name)

    def test_table_create(self):
        table_name = "test_table"
        table_definition = "name text, age numeric(2)"

        self.database.create_table(
            table_name=table_name, table_definitions=table_definition
        )


if __name__ == "__main__":
    test_sql_base.run()
