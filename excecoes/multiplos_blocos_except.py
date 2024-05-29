def ler_numeros_do_arquivo(arquivo):
    numeros = []
    try:
        with open(arquivo, 'r') as file:
            for linha in file:
                numeros.append(int(linha.strip()))
        media = sum(numeros) / len(numeros)
        print(f"Média: {media}")

        
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except ZeroDivisionError:
        print("Erro: Não há números no arquivo.")
    except ValueError:
        print("Erro: Valor inválido encontrado no arquivo.")

ler_numeros_do_arquivo("numeros.txt")
#cria no diretorio que o comando é rodado
