from time import sleep

def decorador(funcao):
    def wrapper(*args, **kwargs):
        print("minha funcao decorada")
        resultado = funcao(*args, **kwargs)
        return resultado
    return wrapper

@decorador
def minha_primeira_atividade():
    message = print("minha primeira atividade - hello world")
    sleep(3)
    return message

minha_primeira_atividade()