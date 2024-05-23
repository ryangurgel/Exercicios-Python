idades = [30, 25, 35]

with open(file=r'python\Exercicios Python\arquivos\idades.csv', mode = "w", encoding = 'utf-8') as fp:
    linha = 'idade\n'
    fp.write(linha)
    for idade in idades:
        linha = str(idade) + '\n'
        fp.write(linha)


#modo "a" append
with open(file=r'python\Exercicios Python\arquivos\idades.csv', mode = "a", encoding = 'utf-8') as fp:
    for idade in idades:
        linha = str(idade + 100) + '\n'
        fp.write(linha)