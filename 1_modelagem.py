# modelagem da Classe
class Pessoas:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    #método
    def logar_sistema(self):
        print(f'{self.nome}, seu login foi Bem Sucedido!')


#Criando instancias
pessoa_1 = Pessoas('Alefe Gomes', 24, '12345678900')
pessoa_2 = Pessoas('Marcos Antonio', 25, '12378945625')

pessoa_1.logar_sistema()
pessoa_2.logar_sistema() 
