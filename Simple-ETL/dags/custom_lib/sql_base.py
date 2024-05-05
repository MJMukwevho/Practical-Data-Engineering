import psycopg2
import json


class sql_base:
    def __init__(self):
        pass

    def sql_runner(self, query):

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
            query = query
            result = cursor.execute(query)

        return result

    def create_schema(self, schema_name):

        query = f"CREATE SCHEMA IF NOT EXISTS {schema_name}"
        response = self.sql_runner(query=query)

        return response

    def create_table(self, table_name, schema_name, table_definitions):

        query = f"""CREATE TABLE IF NOT EXISTS {schema_name}.{table_name}({table_definitions})"""

        self.sql_runner(query)

    def write_record_to_table(self, record):
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

        return None
