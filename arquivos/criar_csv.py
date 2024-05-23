import os

# Dados que queremos escrever no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Profissão'],
    ['João', 30, 'Engenheiro'],
    ['Maria', 25, 'Médica'],
    ['Carlos', 35, 'Professor']
]

# Nome do arquivo CSV
nome_arquivo = 'dados.csv'

# Caminho do diretório onde o script .py está localizado
diretorio_script = r'C:\Users\ryang\OneDrive\Área de Trabalho\Projetos\python\Exercicios Python\arquivos'

# Caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio_script, nome_arquivo)

# Abre o arquivo para escrita
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    # Itera sobre os dados e escreve cada linha no arquivo
    for linha in dados:
        # Junta os elementos da linha em uma string separada por vírgula
        linha_csv = ','.join(map(str, linha))
        # Escreve a linha no arquivo
        arquivo.write(linha_csv + '\n')

print("Arquivo CSV criado com sucesso em:", caminho_arquivo)
