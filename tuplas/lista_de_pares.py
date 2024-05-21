lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

pares = list(zip(lista1, lista2))
print(pares)











pares = [(1, 'a'), (2, 'b'), (3, 'c')]

#operador * é usado para descompactar as tuplas dentro da lista
lista1, lista2 = zip(*pares)
print(lista1) 
print(lista2)  