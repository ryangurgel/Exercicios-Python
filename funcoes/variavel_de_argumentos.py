#assinatura da função
def calcular_media(*args: int) -> float:
    if len(args) == 0:
        return 0.0
    return sum(args) / len(args)


print(calcular_media(2, 4, 6)) 
print(calcular_media(10, 20, 30, 40, 50))  
print(calcular_media())  



####################

def calcular_media(*variaveis: int) -> float:
    if len(variaveis) == 0:
        return 0.0
    return sum(variaveis) / len(variaveis)


print(calcular_media(2, 4, 6)) 
print(calcular_media(10, 20, 30, 40, 50))  
print(calcular_media())  
