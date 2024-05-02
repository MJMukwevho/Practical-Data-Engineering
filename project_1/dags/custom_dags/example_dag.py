import sys
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from custom_lib.sql_base import sql_base


def task1():
    print("Executing task 1")


def task2():
    print("Executing task 2")


# Define the default arguments for the DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 4, 24),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
}

# Instantiate the DAG object
dag = DAG("simple_dag", default_args=default_args, schedule_interval=None)

# Define the tasks
start_task = DummyOperator(task_id="start_task", dag=dag)
task1 = PythonOperator(task_id="create_database", python_callable=task1, dag=dag)
task2 = PythonOperator(task_id="Fetch_data", python_callable=task2, dag=dag)

# Define the task dependencies
start_task >> task1 >> task2
