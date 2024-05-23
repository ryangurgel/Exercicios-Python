class Animal:
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        return "Au Au"

class Gato(Animal):
    def falar(self):
        return "Miau"

def som_do_animal(animal):
    print(animal.falar())

som_do_animal(Cachorro())
som_do_animal(Gato())
