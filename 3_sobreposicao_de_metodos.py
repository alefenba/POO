#A classe pai é chamada atraves do super e cria os atributos de instancias...
#Caso contrario a classe filha irá sempre sobrepor a classe pai


class Pessoa:

    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

class Cliente(Pessoa):

    def __init__(self, id_cliente,nome,cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente
        

class Vendedor(Pessoa):

    def __init__(self,id_vendedor, nome, cpf):
        super().__init__(nome, cpf)
        self.id_vendedor = id_vendedor

c1 = Cliente(2,'Alefe gomes', '12345678')
print(c1.nome)
print(c1.cpf)
print(c1.id_cliente)

print('-----')

v1 = Vendedor(1,'Alf', '789456123')
print(v1.nome)
print(v1.cpf)
print(v1.id_vendedor)

