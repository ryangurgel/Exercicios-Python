# List Comprehensions - Exercícios Resolvidos

# Exercício 1
# Criar uma lista de números de 0 a 9.
numeros = [x for x in range(10)]
print("Exercício 1:", numeros)
# Resultado esperado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Exercício 2
# Criar uma lista de quadrados dos números de 0 a 9.
quadrados = [x**2 for x in range(10)]
print("Exercício 2:", quadrados)
# Resultado esperado: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Exercício 3
# Criar uma lista dos números pares de 0 a 20.
pares = [x for x in range(21) if x % 2 == 0]
print("Exercício 3:", pares)


# Exercício 4
# Criar uma lista dos comprimentos das palavras em uma lista de palavras.
palavras = ["python", "list", "comprehension", "exercises"]
comprimentos = [len(palavra) for palavra in palavras]
print("Exercício 4:", comprimentos)


# Exercício 5
# Criar uma lista de números de 0 a 9, mas substituindo os números ímpares por -1.
substituidos = [x if x % 2 == 0 else -1 for x in range(10)]
print("Exercício 5:", substituidos)


# Exercício 6
# Filtrar uma lista de números, mantendo apenas aqueles que são divisíveis por 3.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
divisiveis_por_3 = [x for x in numeros if x % 3 == 0]
print("Exercício 6:", divisiveis_por_3)


# Exercício 7
# Criar uma lista de pares (número, quadrado) para números de 0 a 9.
pares = [(x, x**2) for x in range(10)]
print("Exercício 7:", pares)


# Exercício 8
# Converter uma lista de strings em uma lista de caracteres.
palavras = ["hello", "world"]
caracteres = [char for palavra in palavras for char in palavra]
print("Exercício 8:", caracteres)


# Exercício 9
# Criar uma lista de listas, onde cada sublista contém números de 0 a 4.
listas = [[x for x in range(5)] for _ in range(3)]
print("Exercício 9:", listas)


# Exercício 10
# Aplanar uma lista de listas em uma única lista.
listas = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
aplanada = [item for sublista in listas for item in sublista]
print("Exercício 10:", aplanada)

# Exercício 11
# Transformar uma lista de strings em uma lista de dicionários com a string e seu comprimento.
strings = ["apple", "banana"]
dicionarios = [{"word": s, "length": len(s)} for s in strings]
print("Exercício 11:", dicionarios)