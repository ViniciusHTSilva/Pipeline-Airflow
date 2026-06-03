from datetime import datetime
from os import mkdir

import pendulum
from airflow.models import DAG
from airflow.providers.standard.operators.empty import EmptyOperator
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.python import PythonOperator


def cumprimentos():
    print("Boas-vindas ao Airflow!")

with DAG(

    dag_id="test_dag",
    #Define a data a partir da qual o Airflow começa a considerar execuções da DAG.
    start_date=pendulum.datetime(2021, 1, 1),
    #É uma expressão Cron que define quando a DAG será executada.
    schedule='@daily'
) as dag:
    # EmptyOperator Não executa nenhuma ação. Serve apenas para organizar o fluxo da DAG.
    tarefa1 = EmptyOperator(task_id = 'Tarefa1')
    tarefa2 = EmptyOperator(task_id = 'Tarefa2')
    tarefa3 = EmptyOperator(task_id = 'Tarefa3')

    # BashOperador roda comandos de Terminal
    tarefa4 = BashOperator(
        task_id='Criar_Pasta',
        bash_command='mkdir -p /tmp/Pipeline-Airflow'
    )
    tarefa5 = BashOperator(
        task_id='Localizacao',
        bash_command='hostname && pwd && whoami'
    )

    tarefa6 = PythonOperator(
        task_id='ExecutarPython',
        python_callable=cumprimentos,

    )

    # Quando a tarefa1 e executada a tarefa dois e tres podem ser executadas.
    tarefa1 >> [tarefa2, tarefa3]
    tarefa3 >> [tarefa4] >> [tarefa5, tarefa6]