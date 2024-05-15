class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
    
    def imprimir_informacoes(self):
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Endereço:", self.endereco)

# Exemplo de uso da classe Pessoa
pessoa1 = Pessoa("João", 30, "Rua A, nº 123")
pessoa1.imprimir_informacoes()

