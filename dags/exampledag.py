import datetime
from time import sleep

from airflow.sdk import dag
from airflow.providers.standard.operators.empty import EmptyOperator


@dag(start_date=datetime.datetime(2025, 8, 15), schedule="@daily")
def minha_primeira_dag():
    message = print("minha primeira atividade - hello world")
    sleep(3)
    return message


minha_primeira_dag()
