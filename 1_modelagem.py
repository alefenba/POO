'''
Atributos de classes São propriedades semelhantes que os objetos de uma classe possuem.
'''

class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = 'Ser Humano'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
        
    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está Logando no sistema')

    @classmethod
    def andar(cls, velocidade):
        print(f'Estou andando na velocidade {velocidade} m/s')

#p1 = Pessoas('Alefe Gomes', 24)
#p2 = Pessoas('Caio sampaio', 21)

Pessoas.andar(10)

