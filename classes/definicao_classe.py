# Programação Orientada a Objetos (POO) é um paradigma da programação que utiliza objetos para modelar partes de um problema do mundo real


class Pessoa: #molde que define um conjunto de propriedades e metodos comuns ao objetos desse tipo
    def __init__(self, nome, idade, endereco): #chama o metodo construtor da classe e inicializa os atributos
        #atributos
        self.nome = nome #acessa os atributos da instancia com o self = instancia atual
        self.idade = idade #Inicializa o atributo com o valor passado como argumento.
        self.endereco = endereco

    #metodo
    def imprimir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Endereço:", self.endereco)

# Exemplo de uso da classe Pessoa
pessoa1 = Pessoa("João", 30, "Rua A, nº 123") #objeto é instansiado com a classe Pessoa e entra na variavel pessoa1
print(pessoa1.endereco)
pessoa1.imprimir_informacoes()


#tudo em python é um objeto, emcapsulamento

