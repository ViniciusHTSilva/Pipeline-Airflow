from datetime import datetime
from os import mkdir

import pendulum
from airflow.models import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

with (DAG(
    dag_id="test_dag",
    #Define a data a partir da qual o Airflow começa a considerar execuções da DAG.
    start_date=pendulum.datetime(2021, 1, 1),
    #É uma expressão Cron que define quando a DAG será executada.
    schedule_interval='0 0 * * *'
) as dag):
    # EmptyOperator Não executa nenhuma ação. Serve apenas para organizar o fluxo da DAG.
    tarefa1 = EmptyOperator(task_id = 'Tarefa1')
    tarefa2 = EmptyOperator(task_id = 'Tarefa1')
    tarefa3 = EmptyOperator(task_id = 'Tarefa3')

    # BashOperador roda comandos de Terminal
    tarefa4 = BashOperator (
        task_id='Criar Pasta',
        Bash_command = 'mkdir -p "/home/vinicius/Documentos/GitHub/pipeline/Pipe-Airlfow"'
    )
    # Quando a tarefa1 e executada a tarefa dois e tres podem ser executadas.
    tarefa1 >> [tarefa2, tarefa3]
    tarefa3 >> [tarefa4]