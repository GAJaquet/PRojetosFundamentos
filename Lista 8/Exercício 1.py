import random

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print(f"Eu sou um animal chamado {self.nome}.")

class Carnivoro(Animal):
    def caca(self):
        print(f"{self.nome} está caçando.")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal carnívoro.")

class Herbivoro(Animal):
    def pastar(self):
        print(f"{self.nome} está pastando.")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal herbívoro.")

class Onivoro(Carnivoro, Herbivoro):
    def comer(self):
        escolha = random.randint(0, 1)
        if escolha == 0:
            self.caca()
        else:
            self.pastar()

    def exibirDescricao(self):
        super().exibirDescricao()
        print("Sou um animal onívoro.")

# Exemplo de uso
leao = Carnivoro("Leão")
vaca = Herbivoro("Vaca")
urso = Onivoro("Urso")

leao.exibirDescricao()
leao.caca()

vaca.exibirDescricao()
vaca.pastar()

urso.exibirDescricao()
urso.comer()
