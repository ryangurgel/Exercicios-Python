try:
    numero = int('dez')
    print(type(numero))
except ValueError:
    print("Erro: não é possível converter a string para inteiro.")
