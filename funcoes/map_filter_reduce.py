#função map aplica uma função em todos os elementos de uma coleção (listas, dicionarios, tuplas...)
#trabalha em paralelo nao exercutando 1 a 1 e sim varios por vez, dependendo do numero de nucleos do processador
#python posterga a execução do map até que seja necessario

lista_de_numeros = [1,2,5,20,6]

numeros_ao_quadrado = map(lambda x: x * 3, lista_de_numeros)

#convertendo para lista a função roda
print(list(numeros_ao_quadrado))



#############################################################################################################



#Sem filter
pares = []
for i in lista_de_numeros:
    if i%2 == 0:
        pares.append(i)

print(pares)


#Com filter
pares = filter(lambda x: x%2 == 0, lista_de_numeros)
print(list(pares))





#################################################################################################################
#pega uma função e aplica em dois itens em todos os elementos


from functools import reduce

maior_numero = reduce(lambda primeiro, segundo : primeiro if primeiro >= segundo else segundo, lista_de_numeros)

print(maior_numero)


#programação funcional é mais pro lado de matematica
#Ao trabalhar com grandes quantidades de dados, usar a função map pode ser mais eficiente do que usar o "for".