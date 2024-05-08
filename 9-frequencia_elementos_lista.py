lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]
frequencia = {}
for i in lista:
    if i in frequencia:
        frequencia[i] += 1
    else:
        frequencia[i] = 1
print(frequencia)