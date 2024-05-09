texto = "Olá, mundo!"

numeros = [4 + ord(letra[:1]) for letra in texto]

print(numeros)

letras = [chr(numeros - 4) for numeros in numeros]

print("".join(letras))