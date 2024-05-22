import sys
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from custom_lib.sql_base import sql_base
from custom_lib.get_data import get_data


def create_db_schema_table():

    database = sql_base()
    database.create_schema(schema_name="users")

    database.create_table(
        schema_name="users",
        table_name="people",
        table_definitions="name text, surname text, title text, gender text, coordinates jsonb, country text, city text",
    )


def load_data():
    database = sql_base()
    _, record = get_data()

    database.write_record_to_table(record=record)


# Define the default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 5, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
}

# Instantiate the DAG object
dag = DAG("simple_ETL", default_args=default_args, schedule_interval="* * * * *")


# Define the tasks
start_task = DummyOperator(task_id="start_task", dag=dag)
task1 = PythonOperator(task_id="task1", python_callable=create_db_schema_table, dag=dag)
task2 = PythonOperator(task_id="task2", python_callable=load_data, dag=dag)

# Define the task dependencies
start_task >> task1 >> task2
