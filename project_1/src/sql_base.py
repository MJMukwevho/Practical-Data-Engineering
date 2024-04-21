import psycopg2


class sql_base:
    def __init__(self):
        pass

    def sql_runner(self, query):
        url = "http://postgres-db:45432/postgres_db"
        # user
        username = "postgres"
        password = "postgres"

        conn_details = psycopg2.connect(
            host="postgres-db",
            database="postgres",
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

    def create_table(self, table_name, table_definitions):

        query = f"""CREATE TABLE IF NOT EXISTS {table_name}({table_definitions})"""

        self.sql_runner(query)
