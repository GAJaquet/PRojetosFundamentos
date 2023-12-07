class UnidadeMilitar:
    def mover(self):
        pass

    def atacar(self):
        pass

class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("Arqueiro se movendo silenciosamente.")

    def atacar(self):
        print("Arqueiro atacando com arco e flecha.")

class Soldado(UnidadeMilitar):
    def mover(self):
        print("Soldado se movendo rapidamente.")

    def atacar(self):
        print("Soldado atacando com espada.")

class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("Cavaleiro montando seu cavalo.")

    def atacar(self):
        print("Cavaleiro atacando com lança.")

#Ações
soldado1 = Soldado()
arqueiro1 = Arqueiro()
cavaleiro1 = Cavaleiro()
unidades = [soldado1, arqueiro1, cavaleiro1]
for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print() 
