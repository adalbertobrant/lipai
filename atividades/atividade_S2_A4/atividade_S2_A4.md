# Atividade S2 A4

**Nome**: Adalberto Caldeira Brant Filho

**Repositório GitHub**: https://github.com/adalbertobrant/lipai

# Código das Videoaulas

## Aula 01 - Funções

  Funções são blocos de códigos, modularizáveis que podem ser reutilizadas, realizando tarefas específicas.
  As funções evitam a duplicação de código
  O python já tem algumas funções que são conhecidas como Standard Library Functions ou built-in functions, essas funções já foram definidas, sendo apenas chamadas
  ex : print, len
  As funções podem ter parametros ou não:
  ```
  def oi(nome):
      print(f'Oi, {nome}')
  ```
  ```python3
  """" Aula 01 - Introdução a funções """

# funções built-in functions

nome = 'José'
print(nome)
print(len(nome))

# User Defined Functions
# são definidas pelo usuário do programa python
# fazem parte da solução do problema

# função saudacoes

def saudacoes():
    print("Hello World")


# para imprimir o resultado da função saudacoes, deve-se chamar a função
saudacoes()
saudacoes()

# imprime saudacao com nome

def ola(nome):
    print(f'Olá, {nome}')


# maria é o argumento do parametro nome

ola('Maria')

# função para calcular a media

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    print(media)


# chamada
# argumentos são literais
calcular_media(10, 5, 7)

n1 = 5
n2 = 7
n3 = 8

# chamada
# argumentos são variáveis
calcular_media(n1, n2, n3)

# Declaração
# nome: media
# parametros: nota1, nota2, nota3
# retorno: media

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3.0

media = media(10, 7, 4)
print(f'Valor da média é {media}')

# quando colocamos um retorno na função ele pode ser usado em diferentes cenários, como salvar em um banco de dados, enviar um email , salvar em um arquivo
```
## Aula 02 -

```python3
""" Aula 02 - Arguments: positional , keyword, default value """

# declara uma função que soma dois números
def somar(n1, n2):
    #   soma = n1 + n2
    #   return soma
    return n1 + n2


# forma de chamar é argumentos posicionais
# argumentos vão de acordo com a posição
print(somar(3.4, 10))

# argumentos nomeados onde o parametro é nomeado com o seu literal
print(somar(n1=5, n2=10))
print(somar(n2=10, n1=5))

# função dividir
def dividir(dividendo, divisor):
    if divisor != 0:
        return dividendo / divisor
    return "Erro de argumento da função"

# argumentos posicionais
print(dividir(10, 2))
print(dividir(divisor=3, dividendo=10))
print(dividir(dividendo=10, divisor=2))
print(dividir(*[0, 0]))

# fazendo unpack de listas ou tuplas e enviando para a função
numeros = [10, 32]
print(f'Somar números de uma lista -> {somar(numeros[0], numeros[1])}')

# *args(lista)

print(f'Somar números de uma lista -> {somar(*numeros)}')
tuplas_numeros = (11, -4)
print(f'Somando tuplas -> {somar(*tuplas_numeros)}')

""" Ao fazer o unpack devemos ter o cuidado que a
coleção enviada deve ter o mesmo tamanho dos argumentos da função """

# unpack de dicionários **kwargs
numeros = {
    'n1': 100.45,
    'n2': 35.86
}
print(f'Soma de dois valores do dicionário -> {somar(**numeros)}')
""" Ao enviar por dicionário ele usa os valores das chaves do dicionário
que tem que ser o mesmo nome dos argumentos que já estão na função """

# valores padrões em uma função
# Declaração
# nome: saudacoes
# parametros: nome-> deve passar obrigatoriamente, saudacao-> terá um valor default
# retorno: string
def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao} {nome} !'


print(saudacoes('João', 'Olá'))
print(saudacoes('Pedro'))
```

