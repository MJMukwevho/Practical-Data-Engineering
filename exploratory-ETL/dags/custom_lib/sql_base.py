"""
This module serves as a boiler-plate code for all things sql
that are ran in python.
"""

import json
import psycopg2


class SqlBase:
    """
    Boiler plate class for sql based operations
    """

    def __init__(self):
        pass

    def sql_runner(self, query: str):
        """
        Creates connections and performs operations on databases
        """

        # db details
        host = "postgres-db"
        database_name = "postgres_db"
        # user
        username = "postgres"
        password = "postgres"

        conn_details = psycopg2.connect(
            host=host,
            database=database_name,
            user=username,
            password=password,
            port="5432",
        )

        with conn_details:
            cursor = conn_details.cursor()
            cursor.execute(query)

            if cursor.description is not None:
                # If it is a select statement, fetch the result
                result = cursor.fetchall()  # Assuming you expect a single row result
                return result  # Assuming the query returns a single value

            return True

    def create_schema(self, schema_name: str):
        """
        Function to create schema on databases
        """

        query = f"CREATE SCHEMA IF NOT EXISTS {schema_name}"
        self.sql_runner(query=query)

    def create_table(
        self, 
        table_name: str, 
        schema_name: str, 
        table_definitions: str,
        ) -> None:
        """
        Function to create database tables
        """

        query = f"""CREATE TABLE IF NOT EXISTS {schema_name}.{table_name}({table_definitions})"""

        self.sql_runner(query)

    def write_record_to_table(
        self, 
        record: dict
        ) -> None:
        """
        function to write records to tables in databases
        """
        schema_name = "users"
        table_name = "people"
        column_names = """name,surname,title,gender,country,city,coordinates"""

        values = (
            record["name"]["first"],
            record["name"]["last"],
            record["name"]["title"],
            record["gender"],
            record["location"]["country"],
            record["location"]["city"],
            json.dumps(record["location"]["coordinates"]),
        )
        insert_statement = (
            f"""INSERT INTO {schema_name}.{table_name}({column_names}) VALUES{values}"""
        )

        self.sql_runner(query=insert_statement)
