with open(file=r'python\Exercicios Python\arquivos\dados.csv', mode='r', encoding='utf-8') as arquivo_meu:
    conteudo = arquivo_meu.read().strip().split(',')
print(conteudo)


##############################


conteudo_lista1 = []
with open(file=r'python\Exercicios Python\arquivos\dados.csv', mode='r', encoding='utf-8') as arquivo_meu:
    for linhab in arquivo_meu:
        linhal = linhab.strip().split(',')
        conteudo_lista1.append(linhal)

print(conteudo_lista1)

##############################

conteudo_lista2 = []
with open(file=r'python\Exercicios Python\arquivos\dados.csv', mode='r', encoding='utf-8') as arquivo_meu:
    readline = arquivo_meu.readline()
    while readline:
        conteudo_lista2.append(linhal)
        readline = arquivo_meu.readline()

print(conteudo_lista2)

##############################

conteudo_dicionario = []
with open(file=r'python\Exercicios Python\arquivos\dados.csv', mode='r', encoding='utf-8') as arquivo_meu:
    #primeira linha, o python remove da leitura no for
    readline = arquivo_meu.readline().strip().split(',') #acha o /n

    for linhab in arquivo_meu:
        linhal = linhab.strip().split(',')
        conteudo_dicionario.append(dict(zip(readline, linhal)))


print(conteudo_dicionario)


##############################

idades = []
with open(file=r'python\Exercicios Python\arquivos\dados.csv', mode = 'r', encoding = 'utf-8') as arquivo:
    linha = arquivo.readline() # Ler o cabeçalho
    linha = arquivo.readline() # Ler a primeira linha de dados

    while linha:
        linha_separada = linha.split(',')
        idade = linha_separada[1]
        idades.append(idade)
        linha = arquivo.readline()

print(idades)

###################

file_path = r'python\Exercicios Python\arquivos\dados.csv'
line_number = 3  

with open(file_path, mode='r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()  # Ler todas as linhas do arquivo em uma lista

# Acessar a linha específica desejada
if line_number < len(linhas):
    linha_especifica = linhas[line_number]
    linha_separada = linha_especifica.split(',')
    idade = linha_separada[1]
    print(f"A idade na linha {line_number} é: {idade}")
else:
    print(f"O arquivo tem menos de {line_number + 1} linhas.")
