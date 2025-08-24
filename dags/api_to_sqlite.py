from airflow.decorators import task, dag
from include.controller import pegar_pokemon, adicionar_pokemon, gerar_numero_aleatorio
from datetime import datetime


@dag(dag_id="capturar_pokemons",
     description="pipeline de coleta de pokemons da api e salva no banco",
     start_date=datetime(2025,8,24),
     schedule="* * * * *",
     catchup=False
     )

def api_sqlite():

    @task(task_id="gerar_numero_aleatorio")
    def task_gerar_numero_aleatorio():
        return gerar_numero_aleatorio()
    
    @task(task_id="pegar_pokemon")
    def task_pegar_pokemon():
        return pegar_pokemon
    
    @task(task_id="adicionar_pokemon")
    def task_adicionar_pokemon():
        return adicionar_pokemon()

    t1 = task_gerar_numero_aleatorio()
    t2 = task_pegar_pokemon(t1)
    t3 = task_adicionar_pokemon(t2)

    t1 >> t2 >> t3

api_sqlite()