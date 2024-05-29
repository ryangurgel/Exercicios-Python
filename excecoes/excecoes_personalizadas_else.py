#definindo a classe, com herença e, Exception, logo, se comportará como qualquer outra exceção
class ErroDeEntradaInvalida(Exception):
    pass



def validar_entrada(valor):
    if not isinstance(valor, int):
        raise ErroDeEntradaInvalida(f"Entrada inválida: {valor}")
#raise levanta uma exceção, interrompe o programa e vai para except
    
ErroDeEntradaInvalida() #cria uma instância da exceção, mas não faz nada com ela

try:
    validar_entrada("fede")
except ErroDeEntradaInvalida as e:
    print(e)
else:
    print("sem erro")


########################################


def sem_isinstance(valor):
    if type(valor) != int:
        print(2)

sem_isinstance(2)


###################


def com_isinstance(valor):
    if not isinstance(valor, int):
        print(2)

com_isinstance("2")


########################################