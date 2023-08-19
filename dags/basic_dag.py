from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(dag_id="basic_dag", schedule_interval="0 0 * * *",
         start_date=datetime(2023,1,1), catchup=False) as basicDag:
    
    basic_bash = BashOperator(
        task_id="bash",
        bash_command="echo My First Dag!"
    )