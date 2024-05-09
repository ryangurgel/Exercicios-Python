#Crie uma lista com cinco números inteiros e faça as seguintes operações: adicionar um número ao final, remover o segundo elemento e imprimir a lista final.


lista = []

#lista.append('1item')
#lista.append('2item')

lista.extend(['1item', '2item', '3item', '4item'])

lista.append('5item')
lista.pop(1)
#del numbers[1]

print(lista)