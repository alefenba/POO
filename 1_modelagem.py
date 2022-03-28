'''
CLS é um parametro a qual recebe o estado da classe 
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
    def andar(cls):
        cls.possui_boca = False
        return None

#p1 = Pessoas('Alefe Gomes', 24)
#p2 = Pessoas('Caio sampaio', 21)

print(Pessoas.possui_boca)
Pessoas.andar()
print (Pessoas.possui_boca)

