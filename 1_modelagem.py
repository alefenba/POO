'''
 O self é sempre usado para referenciar instancia...
Através do self eu consigo saber de qual instacia aquele método/atributo está sendo chamado.
'''

class Pessoas:
    def __init__(self, nome,):
        self.nome = nome
        
    def retorna_nome(self):
        return self.nome

    def logar_sistema(self):
        print(f'{self.retorna_nome()} Está Logando no sistema')


pessoa_1 = Pessoas('Alefe Gomes')
pessoa_1.logar_sistema()


