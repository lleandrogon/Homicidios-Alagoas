from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

from datetime import datetime
import pendulum

from operators.extractHomicidiosAl import extract_homicidios
from operators.transformHomicidiosAl import transform_homicidios
from operators.createTableHomicidiosAl import query

dag = DAG(
    dag_id = "Homicidios_Alagoas",
    schedule = "0 21 * * *",
    default_args = {
        "owner": "Airflow",
        "retries": 1,
        "start_date": pendulum.datetime(2025, 10, 1, tz = "America/Sao_Paulo")
    },
    catchup = False,
    tags = ["alagoas, al"]
)

e_homicidios = PythonOperator(
    task_id = "extract_homicidios",
    python_callable = extract_homicidios,
    dag = dag
)

t_homicidios = PythonOperator(
    task_id = "transform_homicidios",
    python_callable = transform_homicidios,
    dag = dag
)

ct_homicidios = SQLExecuteQueryOperator(
    task_id = "create_table_homicidios",
    conn_id = "homicides",
    sql = query,
    dag = dag
)

e_homicidios >> t_homicidios >> ct_homicidios