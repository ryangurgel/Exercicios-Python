def busca_binaria(lista, elemento):
    esquerda, direita = 0, len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        # Verifica se o elemento está no meio
        if lista[meio] == elemento:
            return meio
        # Se o elemento for maior, ignora a metade esquerda
        elif lista[meio] < elemento:
            esquerda = meio + 1
        # Se o elemento for menor, ignora a metade direita
        else:
            direita = meio - 1

    # Se o elemento não estiver presente
    return -1

# Exemplo de uso
lista_ordenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
elemento_procurado = 7

resultado = busca_binaria(lista_ordenada, elemento_procurado)

if resultado != -1:
    print(f'Elemento encontrado no índice {resultado}.')
else:
    print('Elemento não encontrado na lista.')
