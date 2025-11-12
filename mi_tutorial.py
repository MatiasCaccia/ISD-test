from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="mi_tutorial_dag",
    description="DAG de práctica basado en el tutorial oficial",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["mia", "practica", "tutorial"],
) as dag:

    start = EmptyOperator(
        task_id="start",
    )

    print_date = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    print_hello = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hola Airflow desde MIA!'",
    )

    end = EmptyOperator(
        task_id="end",
    )

    # Definición de dependencias (orden de ejecución)
    start >> print_date >> print_hello >> end
