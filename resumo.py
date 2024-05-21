import os

def summarize_python_files(directory):
    # Caminho para o arquivo de resumo que será criado
    summary_path = os.path.join(directory, 'summary.txt')
    
    with open(summary_path, 'w', encoding='utf-8') as summary_file:
        # Itera por todos os diretórios e arquivos
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith('.py'):
                    file_path = os.path.join(root, filename)
                    # Anota o nome do arquivo no arquivo de resumo
                    summary_file.write(f'Nome do arquivo: {file_path}\n')
                    
                    # Abre e lê o conteúdo do arquivo Python com a codificação UTF-8
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        # Anota o conteúdo do arquivo no arquivo de resumo
                        summary_file.write('Conteúdo:\n')
                        summary_file.write(content)
                        summary_file.write('\n\n')  # Espaços entre conteúdos de arquivos diferentes

# Chamada da função especificando o diretório desejado
summarize_python_files(r'C:\Users\ryang\OneDrive\Área de Trabalho\Projetos\python\Exercicios Python')
