class Animal():
    def andar(self):
        print('Estou andando como um animal')
    

    def correr(self):
        print('Estou correndo')


    def pular(self):
        print('Estou pulando')


class Felino:
    def felino(self):
        print('Eu sou um felino')


class Gato(Felino,Animal):
    def miar(self):
        print('Miauuuu')


class Cachorro(Animal):
    def latir(self):
        print('Au Au Au')

y = Gato()
y.andar()
