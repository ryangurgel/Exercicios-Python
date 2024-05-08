pessoa = {'nome': 'Jao', 'idade': 28, 'cidade': 'Fortaleza'}

pessoa['profissão'] = 'Engenheiro'
pessoa['profissão'] = 'teste'



for i,e in pessoa.items():
    print(f"Chave: {i}, Valor: {e}")