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

    @task
    def minha_primeira_atividade():
        print("minha_primeira_atividade")
        sleep(5)

    @task
    def minha_segunda_atividade():
        print("minha_segunda_atividade")
        sleep(5)

    @task
    def minha_terceira_atividade():
        print("minha_terceira_atividade")
        sleep(5)

    @task
    def minha_quarta_atividade():
        print("Pipeline Finalizou!")

    t1 = minha_primeira_atividade()
    t2 = minha_segunda_atividade()
    t3 = minha_terceira_atividade()
    t4 = minha_quarta_atividade()

    t1 >> t2 >> t3 >> t4  # dependências

pipeline()

