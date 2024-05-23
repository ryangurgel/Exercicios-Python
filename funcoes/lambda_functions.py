#função anonima do paradigma funcional
variavel = lambda x: x**2

print(variavel(4))

################

variavel = lambda x: True if x%2 == 0 else False

print(variavel(3))


##############
#funções de alta ordem: funções que recebem funções
#gerar funções dinamicamente

def divisivel(div:int):
    return lambda nun: True if nun%div == 0 else False

divisivel3 = divisivel(div = 3)
divisivel2 = divisivel(div = 2)

print(divisivel3(5))
print(divisivel2(5))