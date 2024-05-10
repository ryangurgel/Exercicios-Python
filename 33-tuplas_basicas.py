tupla = (10, "texto", [1, 2, 3], {'a': 1, 'b': 2})


print("Elementos da tupla:")
for elemento in tupla:
    print()
    print(f'Elemeto: {elemento}')
    print(type(elemento))


try:
    tupla[0] = 20  
except TypeError as e:
    print("Erro ao tentar modificar a tupla:", e)

#Desempacotamento 
a, b, c, d = tupla

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

