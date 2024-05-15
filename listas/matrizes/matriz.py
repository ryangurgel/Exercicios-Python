#Usando listas aninhadas para fazer uma matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    print(linha)

print(matriz[0][1])


listas = [[i * j for j in range(5)] for i in range(3)]
for k in listas:
    print(k)