import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

sys.path.append('/opt/airflow/api_request')

from insert_records import main

default_args = {
    'description':'A DAG to orchestrate data',
    'start_date':datetime(2024, 4, 30),
    'catchup':False,
}

dag = DAG(
    dag_id='weather-api-orchestrator',
    default_args=default_args,
    schedule=timedelta(minutes=5)  # Define your schedule here
)

with dag:
    task1 = PythonOperator(
        task_id='ingest_data_task',
        python_callable=main
    )