""" Aula 06 - equal e hash code """


class Pessoa():
    """ Cria um objeto da classe pessoa """

    def __init__(self, cpf, nome):
        """ construtor da classe pessoa com nome como parametro"""
        self.cpf = cpf
        self.nome = nome

    def __eq__(self, value):
        """ retorna verdadeiro ou falso para certo value """
        if isinstance(value, self.__class__):
            return self.cpf == value.cpf

        return False

    def __hash__(self):
        """ retorna o hash do atributo escolhido """
        return hash(self.cpf)

    def __repr__(self):
        """retorna o objeto em sua forma canônica """
        return f'Pessoa({self.cpf}, {self.nome})'

    def __str__(self):
        """ retorna o objeto em sua forma de string """
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}]'


pessoa1 = Pessoa('123456890-11', 'João')
pessoa2 = Pessoa('123321123-11', 'João')
# pessoa3 tem os mesmos valores de pessoa2
pessoa3 = Pessoa('123321123-11', 'João')

pessoas = {pessoa1, pessoa2, pessoa3}

# imprime o set pessoas
print()
print(pessoas)
print()

# imprime a lista de pessoas
lista_pessoas = [pessoa1, pessoa2, pessoa3]

print()
print(lista_pessoas)
print()

# imprime a quantidade de pessoas na lista
print(lista_pessoas.count(pessoa3))
