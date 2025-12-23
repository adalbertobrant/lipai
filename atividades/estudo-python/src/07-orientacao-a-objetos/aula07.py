""" Aula 07 - Relacionamentos entre classes """


class Endereco:
    """ Endereço de uma localidade """

    def __init__(self, cep, numero):
        """ Construtor do endereço que tem cep e número """
        self.cep = cep
        self.numero = numero

    def __str__(self):
        """ Retorna a representação do objeto da classe Endereco """
        return f'Endereco[cep={self.cep}, numero={self.numero}]'


class Telefone:
    """ Classe de um objeto do tipo telefone """

    def __init__(self, ddd, numero):
        """ Construtor do telefone com ddd e número """
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        """ Retorna a string do objeto da classe Telefone """
        return f'Telefone[ddd={self.ddd}, numero={self.numero}]'


class Pessoa:
    """ Classe pessoa com nome, cpf e telefone """

    def __init__(self, nome, cpf, telefone):
        """ Construtor da classe pessoa com none, cpf, telefone """
        self.cpf = cpf
        self.nome = nome
        self.telefone = telefone
        # passar um endereço para a pessoa
        self.enderecos = []

    def add_endereco(self, endereco):
        """ adiciona um endereço ao objeto pessoa """
        self.enderecos.append(endereco)

    def print_enderecos(self):
        """ Imprime o endereço associado ao objeto pessoa """
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        """retorna a string do objeto pessoa """
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}]'


pessoa = Pessoa('João da Silva', '12312312333', '11-99999-0000')
print(pessoa)
print(pessoa.nome, pessoa.cpf, pessoa.telefone)

# Passando um telefone como classe Telefone
print('Acessando Classe Telefone')
pessoa1 = Pessoa('Maria da Silva', '111111111-11', Telefone('21', '5467-1290'))
print(pessoa1)
print(pessoa1.nome, pessoa1.cpf, pessoa1.telefone.ddd, pessoa1.telefone.numero)

# criando um objeto telefone e atribuindo a diferentes pessoas
tel = Telefone('33', '98765-7520')
pessoa3 = Pessoa('José da Silva', '222222222-22', tel)
pessoa4 = Pessoa('Ana da Silva', '333333333-33', tel)

print('pessoas com mesmo telefone')
print(pessoa3)
print(pessoa4)

# adicionando endereços a pessoas criadas

pessoa.add_endereco(Endereco('12345-890', 450))
pessoa.add_endereco(Endereco('23456-789', 759))

local = Endereco('78909-786', 515)

pessoa1.add_endereco(local)
pessoa3.add_endereco(local)
pessoa4.add_endereco(local)

# imprimindo endereços
print(pessoa1)
print(pessoa3)
print(pessoa4)

# imprimindo endereços com um método específico
pessoa1.print_enderecos()
pessoa3.print_enderecos()
