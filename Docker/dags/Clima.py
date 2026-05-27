from airflow import DAG
#Pendulum manipulação de datas e horários
import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    "Dados_Clima",
    dag_id="Clima",
    start_date=pendulum.datetime(2020, 1, 1, tz="America/Sao_Paulo"),
    schedule_interval='0 0 * * 1', #executar toda segunda

)as dag:

    tarefa_1 = EmptyOperator(task_id="tarefa_1")
    tarefa_2 = EmptyOperator(task_id="tarefa_2")
    tarefa_3 = EmptyOperator(task_id="tarefa_3")
    tarefa_4 = BashOperator(
        task_id="Criar_Pasta",
        bash_command= 'mkdir -p "/home/vinicius/Documentos/GitHub/pipeline/"'
    )

    tarefa_1 >>[tarefa_2, tarefa_3]
    tarefa_3 >>[tarefa_4]