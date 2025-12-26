""" Aula 08 - Herança entre classes super() """


class Pessoa():  # SUPER CLASSE
    """ Define uma classe pessoa com oa atributos, cpf, nome , sobrenome """

    def __init__(self, nome, sobrenome, cpf):
        """ Construtor da classe com nome, sobrenome e cpf """
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def obtem_nome_completo(self):
        """ retorna o nome completo da pessoa """
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):  # SUB CLASSE
    """ Classe cliente feita usando herança """

    def __init__(self, nome, sobrenome, cpf):
        """ método construtor da sub classe cliente """
        super().__init__(nome, sobrenome, cpf)
        self.compras = []


class Funcionario(Pessoa):
    """ Classe Funcionario que herda informações da classe pessoa """

    def __init__(self, nome, sobrenome, cpf, salario):
        """ método construtor do objeto funcionario com o salário """
        super().__init__(nome, sobrenome, cpf)
        self.salario = salario

    def calcula_pagamento(self):
        """ método de cálculo de pagamento do funcionário """
        return self.salario - self.salario * 0.1


class Programador(Funcionario):
    """ Classe progamador """

    def __init__(self, nome, sobrenome, cpf, salario, bonus):
        """ construtor da classe programador"""
        super().__init__(nome, sobrenome, cpf, salario)
        self.bonus = bonus

    def calcula_pagamento(self):
        """ método para o cálculo de salário do programador com o bonus usando super() """
        return super().calcula_pagamento() + self.bonus


cliente = Cliente("João", "da Silva", "111.111.111-11")

print(cliente.obtem_nome_completo(), type(cliente))

funcionario = Funcionario("Maria", "da Silva", "222.222.222-22", 2000.45)

print(funcionario.obtem_nome_completo(), funcionario.calcula_pagamento(),
      funcionario.salario, type(funcionario))

prog = Programador("José", "Lopes da Silva", "333.333.333-33", 5000.00, 300.00)

print(prog.obtem_nome_completo())
print(prog.calcula_pagamento())
print(type(prog))
