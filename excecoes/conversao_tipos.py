strings = ["10", "20", "trinta", "40", "cinquenta"]

for iten in strings:
    try:
        numero = int(iten)
        print(f"Convertido: {numero}")
    except ValueError:
        print(f"Erro ao converter: {iten}")