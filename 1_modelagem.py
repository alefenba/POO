
class Pessoas:
    def __init__(self, nome, idade, cpf):
        print(f'{nome} | {idade} | {cpf}')
        

    def logar_sistema(self):
        print('Estou logando no sistema!')

#Sempre que criado uma nova instancia o método construtor será executado
pessoa_1 = Pessoas('Alefe Gomes', 24, '12345678978')


