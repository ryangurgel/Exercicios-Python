class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome} {self.idade} {self.endereco}"

    def __repr__(self):
        return f'Pessoa("{self.nome}", "{self.idade}", {self.endereco})'

pessoa1 = Pessoa("João", 30, "Rua A, nº 123")
print(pessoa1)
print(repr(pessoa1))