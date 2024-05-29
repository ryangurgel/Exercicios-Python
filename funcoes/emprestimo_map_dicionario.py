from functools import reduce

emprestimos = []
with open(file=r'C:\Users\ryang\OneDrive\Área de Trabalho\Projetos\python\Exercicios Python\funcoes\credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline() #atribuindo a primeira linha de dados a variavel
	
	while linha:
		linha_emprestimo = {} #dicionario
		linha_elementos = linha.strip().split(sep=',') #remove /n e divide em ','
		linha_emprestimo['id_vendedor'] = linha_elementos[0] # Atribui o primeiro elemento da lista `linha_elementos` à chave 'id_vendedor' no dicionário
		linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
		linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo) #adiciona o dicionario da linha a lista emprestimos
		linha = fp.readline() #lê a proxima linha pro loop while




valor_emprestimos_map = list(map(lambda x: float(x['valor_emprestimos']), emprestimos)) # map aplica lambda em cada item da lista "emprestimos" e atribui x a cada item, e traz o valor baseado na chave "valor_emprestimos" para cada item 

print(valor_emprestimos_map)




#################################################

#filtrando valores maiores que zero
valor_emprestimos_filtrado = list(filter(lambda x: x > 0, valor_emprestimos_map))



#################################################

#Media
soma_todos = reduce(lambda a,b: a+b, valor_emprestimos_filtrado)
media = soma_todos/len(valor_emprestimos_filtrado)
print(media)


#################################################
#calculando desvio padrão amostral, que tem que usar a correção de Bessel
#ja no Desvio Padrão Populacional nao precisa do berssel


quadrado_diferencas = map(lambda x: (x - media) ** 2, valor_emprestimos_filtrado)

soma_quadrado_diferencas = reduce(lambda a,b: a+b, quadrado_diferencas)

desvio_padrao_emprestimos = (soma_quadrado_diferencas / (len(valor_emprestimos_filtrado) - 1)) ** 0.5

print(desvio_padrao_emprestimos)


#correção de Bessel ajusta a estimativa da variância e do desvio padrão para amostras, tornando-a não tendenciosa