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

## Aula 05 - Métodos especiais

```python3
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
```

    O eval é uma função que serve para executar um código python, ela é muito poderosa trazendo muita responsabilidade ao programador, entretanto pode ser útil em casos especiais.
    A função repr() retorna o objeto canônico criado por def __repr__(self).

## Aula 06 - equal e hash code

```python3
""" Aula 06 - equal e hash code """

# Tanto em python quanto em outras linguagens temos formas de comparação

NOME1 = 'João'
NOME2 = 'João'

# avalia se duas strings são verdadeiras
print(NOME1 == NOME2)


class Pessoa():
    """ Cria um objeto da classe pessoa """

    def __init__(self, nome):
        """ construtor da classe pessoa com nome como parametro"""
        self.nome = nome


pessoa1 = Pessoa('João')
pessoa2 = Pessoa('João')

# comparação entre pessoa1 e pessoa2
print(pessoa1 == pessoa2)

print(pessoa1)
print(pessoa2)

```
Figura 1 mostra a comparação entre duas strings com conteúdo iguais , dando verdadeiro.
![Duas strings nome1 e nome2 com conteúdo iguais](../../../imgs/atividade_S3_A3/aula06-001.png)

Na figura 2 temos que a construção de um objeto pessoa1 possui um endereço de memória específico
![Endereço de memória pessoa1](../../../imgs/atividade_S3_A3/aula06-002.png)

E na figura 3 observamos que apesar do conteúdo ou seja o nome das pessoa1 ser igual ao nome da pessoa2 a comparação utilizando o ' == ' mostra dois endereços de memória diferentes, retornando a opção false no python
![Comparação entre objetos](../../../imgs/atividade_S3_A3/aula06-003.png)

    Para utilizarmos uma comparação da forma que comparamos entre duas strings, devemos sobreescrever o método __eq , definido em python.
```python3
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


pessoa1 = Pessoa('123456890-11', 'João')
pessoa2 = Pessoa('123321123-11', 'João')

# comparação entre pessoa1 e pessoa2
print(pessoa1 == pessoa2)
```
![Método __eq__()](../../../imgs/atividade_S3_A3/aula06-004.png)
   A figura nos mostra que sobreescrevendo o método __eq__() o python interpreta o sinal ' == ' da forma esperada, isso vai ser importante ao fazermos análise de coleções no python.

   Ao termos um conjunto de dados em python, digamos um set da Classe Pessoa, chamado de pessoas, é importante já termos definido como será a comparação, visto que os sets são elementos que nesse caso são objetos que não podem ser iguais veja o exemplo abaixo:
```python3
```
   Nesse exemplo percebemos o seguinte erro ao executarmos o programa:
![Erro hashable](../../../imgs/atividade_S3_A3/aula06-005.png)

   O erro de unshable type 'Pessoa' ocorre, pois ainda não definimos no nosso código como o compilador python deve interpretar um conjunto de objetos pessoa, então ele declara que não se tem um hash para o objeto, devemos proceder a sobreescrita do método ____hash____(), como no código abaixo:
```python3
def __hash__(self):
        """ retorna o hash do atributo escolhido """
        return hash(self.cpf)
```
   Ao executarmos o código completo, percebemos que o set é impresso na tela de forma adequada, removendo o elemento que está repetido, segundo os parâmetros estabelecidos no método ____eq____():
![Set hashable](../../../imgs/atividade_S3_A3/aula06-006.png)

   Ao usarmos a impressão de sets, precisamos de passar a forma canônica para a tela o mesmo não ocorre caso a nossa coleção seja por exemplo uma lista, como na figura abaixo:
![Lista de pessoas](../../../imgs/atividade_S3_A3/aula06-007.png)

   Observe que devemos para a lista usar o método ____str____(), como no código abaixo:
```python3
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
```
    Se utilizarmos o método count ( elemento_a_ser_contado ) para contarmos a quantidade de lista_pessoas em nossa lista, escolhendo por exemplo a pessoa2, teremos como retorno do método de contagem a quantidade de 2, isso indica que o método count avaliada os atributos de cada objeto seguindo a regra estabelecida pelo método sobreescrito ____eq___().

## Aula 07 - Relacionamentos entre classes

```python3
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

    def __str__(self):
        """retorna a string do objeto pessoa """
        return f'Pessoa[cpf={self.cpf}, nome={self.nome}, telefone={self.telefone}], endereço={self.enderecos}'


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
```
![Figura 1- problema dos endereços](../../../imgs/atividade_S3_A3/aula07-001.png)

    A impressão dos endereços vai aparecer como um endereço de uma memória e não sua string,  devemos refatorar a representação e criar um método para exibir a lista de endereços.
    Refaforando o código na classe pessoa e inserindo o método print_enderecos(), nosso código fica assim:
```python3
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
```
![Imprimindo endereços com um método print_enderecos()](../../../imgs/atividade_S3_A3/aula07-002.png)
