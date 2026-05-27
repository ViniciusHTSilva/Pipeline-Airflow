from datetime import datetime
import pendulum
from airflow.models import DAG

with DAG(
    dag_id="test_dag",
    start_date=pendulum.datetime(2021, 1, 1),
    schedule_interval='0 0 * * *'
) as dag: