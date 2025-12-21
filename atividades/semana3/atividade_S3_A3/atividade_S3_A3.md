# Atividade S3 A3

**Nome**: Adalberto Caldeira Brant Filho  
**Repositório GitHub**: https://github.com/adalbertobrant/lipai

## Código das Videoaulas

## Aula 01 - Introdução a Orientação a objetos

A Orientação a objetos é um paradigma de programação, ela consegue representar os dados e também as funções de algo, veja o exemplo abaixo que não é orientado a objetos:

```python3
# calcule a área e perimetro do retangulo


def calcular_area(retangulo):
    """ retorna a área do retângulo """
    return retangulo['base'] * retangulo['altura']


def calcular_perimetro(retangulo):
    """ retorna o perimetro de um retangulo """
    return 2 * (retangulo['base'] + retangulo['altura'])


# declaração dos retângulos

retangulo1 = {
    'base': 10.0,
    'altura': 5.0
}

retangulo2 = {
    'base': 6.0,
    'altura': 3.0
}

print(f'Area retangulo 1 {calcular_area(retangulo1)}')
print(f'Perimetro retangulo 1 {calcular_perimetro(retangulo1)}')
print()
print(f'Area retangulo 2 {calcular_area(retangulo2)}')
print(f'Perimetro retangulo 1 {calcular_perimetro(retangulo1)}')
```
Nesse código que usa o paradigma estruturado, observamos que não temos condições de aproveitar muito o código e que a inserção de novas variáveis retangulo deve ser feita dentro do próprio programa em questão. A estrutura que armazena os dados (variáveis), está separada dos algoritmos que efetuam os cálculos.
Observe o mesmo programa agora escrito em orientação a objetos:

```python3
# Classe representa um conceito
# Classe representa um retangulo
# Classe possui atributos: base e altura
# Classe possui métodos
class Retangulo:
    """ Classe Retangulo """
# criação de métodos de instância

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """ retorna a área do retângulo """
        return self.base * self.altura

    def calcular_perimetro(self):
        """ retorna o perimetro de um retangulo """
        return 2 * (self.base + self.altura)


# instanciando objetos dos tipo retangulo
# chamando o método construtor da classe
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)

print(type(retangulo1))

print(retangulo1.base, retangulo1.altura)
print(type(retangulo1.base), type(retangulo1.altura))

print(retangulo2.base, retangulo2.altura)

print(f"Área retangulo 1 -> {retangulo1.calcular_area()}")
print(f"Área retangulo 2 -> {retangulo2.calcular_area()}")
```
## Aula 02 - Atributos de classe e instância

   Atributos de instância são atributos que associamos a um objeto específico 
   Atibutos de Classes está associado a classe do objeto e normalmente são valores já definidos, o acesso ao atributo de classe é feito usando o nome da classe e a variável ou então no objeto criado e a variável da classe.
   Caso o atributo de classe seja mudado na instância ele é refletido apenas na instância criada.
```python3

""" Aula 02 - Atributos de classe e instância """


class Pessoa:
    """ Classe Pessoa """

    # atributo de classe
    especie = 'Humano'

    def __init__(self, nome, email):
        """ atributos de instância: nome , email """
        self.nome = nome
        self.email = email


pessoa1 = Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = Pessoa('João Santos', 'joao@email.com')

# imprimir dados da Pessoa
print(pessoa1.nome, pessoa1.email)
print(pessoa2.nome, pessoa2.email)
print('------')
# dados da pessoa com atributo de classe
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
print('------')
# dados de atributo de classe acessando a classe
print(Pessoa.especie)
print('------')
# alterar um atributo de classe na instância (objeto) altera somente para aquela instância
print("Alterando pessoa1.especie para alien")
pessoa1.especie = 'Alien'
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print('------')
# alterar um atributo de classe na classe altera para todos os objetos e na classe também.
# desde que aquela instância gerada não tenha sido alterada anteriormente.
Pessoa.especie = "Anunakis"
print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)
```
![Alterando atributos de classe](../../../imgs/atividade_S3_A3/aula02-001.png)
   A figura mostra a alteração do atributo de classe note que a pessoa1 manteve o atributo anteriormente designado para ela.

## Aula 03 - Métodos de classe

   Métodos de classe são executados sem precisar de uma instância de uma classe, podem ser usados para criar um objeto de uma forma mais conveniente ou gerenciar um recurso compartilhado.
   O @classmethod é um método de classe e não de instância ele é um decorator da linguagem python
   O acesso ao método da classe se dá usando o nome da classe e seu método, veja o código abaixo:
```python3
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
```

## Aula 04 -Propriedades

   Servem para ajudar no controle de acesso das instâncias bem como determinar atribuições válidas, são formas personalizadas de obter e alterar os valores de um atributo.
```python3
""" Aula 04 - Propriedades """

# forma de controle de acesso aos atributos de uma instância
# property é um decorator em python que ajuda na validação
# usamos um método com o mesmo nome do atributo com a anotação @property


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


retangulo = Retangulo.from_list((10, 8))

print(retangulo.base, retangulo.altura)
```


