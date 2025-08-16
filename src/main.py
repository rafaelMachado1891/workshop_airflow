from datetime import sleep

def minha_primeira_atividade():
    message = print("minha primeira atividade - hello world")
    sleep(3)
    return message

def minha_primeira_dag():
    message = print("minha segunda atividade - hello world")
    return message

def airflow_primeiro_teste():
    message = print("minha terceira atividade - hello world")
    return message

def decorador(funcao):
    def wrapper(*args, **kwargs):
        print("criei um decorador")
        resultado = funcao(*args, **kwargs)
        return resultado
    return wrapper

@decorador
def minha_primeira_atividade():
    message = print("minha primeira atividade - hello world")
    sleep(3)
    return message

