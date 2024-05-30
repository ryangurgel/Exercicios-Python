class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

class Profissional(Pessoa):
    def __init__(self, nome, idade, endereco, profissao, localdetrabalho):
        super().__init__(nome, idade, endereco)    #pega os atributos da classe herdada
        self.profissao = profissao
        self.localdetrabalho = localdetrabalho 
    
    def __str__(self):
        return f"{self.nome} {self.idade} {self.endereco} {self.localdetrabalho} {self.profissao}"

    def __repr__(self):
        return f'Profissional("{self.nome}", "{self.idade}", "{self.endereco}", "{self.profissao}", "{self.localdetrabalho}")'


p1 = Profissional("João", 30, "Rua 1", "Engenheiro", "Empresa A")
print(p1)  
print(repr(p1))  
