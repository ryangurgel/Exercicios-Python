def calcular_media(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(calcular_media(2, 4, 6)) 
print(calcular_media(10, 20, 30, 40, 50))  
print(calcular_media())  
