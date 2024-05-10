#Crie uma lista com cinco números inteiros e faça as seguintes operações: adicionar um número ao final, remover o segundo elemento e imprimir a lista final.


lista = []

#Adiciona os elementos de outra lista ao final da lista atual.
lista.extend(['1item', '2item', '3item', '4item', 'a'])

#Adiciona um elemento ao final da lista.
lista.append('5item')

# insert(): Insere um elemento em uma posição específica da lista.
lista.insert(0, '0item')

#Remove a primeira ocorrência de um elemento específico da lista.
lista.remove("3item")

#Inverte a ordem dos elementos na lista.
lista.reverse()

#Ordena os elementos da lista.
lista.sort()

#Remove e retorna o elemento de uma posição específica da lista (ou o último elemento se nenhum índice for especificado).
elemento_removido = lista.pop(1)

print(elemento_removido)
print(lista)

#Remove todos os elementos da lista.
lista.clear()

