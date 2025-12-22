""" Aula 05 - Métodos especiais """

# __str__(self)
# representação do objeto como string para humanos

# __repr__(self)
# representação do objeto como string para recriar o objeto, usado para log ou debug
# representação canônica do objeto


class Retangulo:
    """ Classe retangulo """

    def __init__(self, base, altura):
        """ construtor classe retangulo """
        self.base = base
        self.altura = altura

    @property
    def base(self):
        """ getter """
        return self._base

    @base.setter
    def base(self, value):
        """ setter """
        # cria uma validação para valores apenas maiores que zero
        if value <= 0.0:
            raise ValueError('A base deve ser maior que zero')
        self._base = value

    @property
    def altura(self):
        """ getter """
        return self._altura

    @altura.setter
    def altura(self, value):
        """ setter """
        if value <= 0.0:
            raise ValueError('Altura deve ser maior do que zero')
        self._altura = value

    @classmethod
    def from_list(cls, lista):
        """ cria uma instância usando o decorator classmethod a partir de uma lista"""
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        """ cria uma instância a partir de uma string """
        base, altura = rep_retangulo.split(sep=',')
        return cls(float(base), float(altura))

    def calcular_area(self):
        """ retorna a área do retângulo """
        return self.base * self.altura

    def calcular_perimetro(self):
        """ retorna o perimetro de um retangulo """
        return 2 * (self.base + self.altura)

    def __str__(self):
        """ retorna a representação do objeto do retangulo """
        return f'Retangulo[base={self.base}, altura={self.altura}]'

    def __repr__(self):
        """ retorna e recria um objeto canônico do retangulo """
        return f'Retangulo({self.base}, {self.altura})'


retangulo1 = Retangulo(10.0, 5.35)

print(retangulo1.__str__())

print(retangulo1.__repr__)

retangulo2 = retangulo1.__repr__()

print(retangulo2)
print(type(retangulo2))

retangulo2 = eval(retangulo2)
print(retangulo2)
print(type(retangulo2))

retangulo2 = eval(repr(retangulo2))
print(retangulo2)
print(type(retangulo2))
