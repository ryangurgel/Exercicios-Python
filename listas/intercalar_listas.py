lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
intercalada = []
for i in range(len(lista1)):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])
print(intercalada)
