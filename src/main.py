def minha_funcao_decorada(funcao):
    def funcao_wrapper():
        print("criei um decorador")
        funcao()
    return funcao_wrapper

@minha_funcao_decorada
def minha_primeira_atividade():
    print("minha primeira atividade - hello world")

minha_primeira_atividade()
    