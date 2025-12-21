""" Aula 03 - Métodos de classe """

# calcule a área e perimetro do retangulo


class Retangulo:
    """ Classe retangulo """

    def __init__(self, base, altura):
        """ construtor classe retangulo """
        self.base = base
        self.altura = altura

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


retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)

# cria uma instância de um objeto Retangulo
print('--- Retangulo 3 --- ')
retangulo3 = Retangulo.from_list((3, 4))
print('Retangulo criado pelo método de classe usando @classmethod ->decorator')
print(f'base -> {retangulo3.base} altura -> {retangulo3.altura}')
print(
    f'Area -> {retangulo3.calcular_area()}\nPerimetro -> {retangulo3.calcular_perimetro()}')

# cria uma instância de um objeto Retangulo por meio de uma string
print('--- Retangulo 4 ---')
retangulo4 = Retangulo.from_string("5.5,3.6")
print('Retangulo criado pelo método de classe usando @classmethod ->decorator')
print(f'base -> {retangulo4.base} altura -> {retangulo4.altura}')
print(
    f'Area -> {retangulo4.calcular_area()}\nPerimetro -> {retangulo4.calcular_perimetro()}')


# imprimir na tela área e perimetro retangulo1
print('---- Retangulo 1 ----')
print(retangulo1.calcular_area())
print(retangulo1.calcular_perimetro())
