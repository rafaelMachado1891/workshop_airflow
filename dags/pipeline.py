from time import sleep
from airflow.decorators import dag, task
from datetime import datetime


@dag(
        dag_id="minha_pipeline",
        description="minha etl",
        schedule="* * * * *",
        start_date=datetime(2025,8,17),
        catchup=False #backfill        
)
def pipeline():

    def minha_primeira_atividade():
        print("minha_primeira_atividade")
        sleep(5)

    def minha_segunda_atividade():
        print("minha_segunda_atividade")
        sleep(5)

    def minha_terceira_atividade():
        print("minha_terceira_atividade")
        sleep(5)

    def minha_quarta_atividade():
        print("Pipeline Finalizou!")

    def pipeline():
        minha_primeira_atividade()
        minha_segunda_atividade()
        minha_terceira_atividade()
        minha_quarta_atividade()