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

# unpack de dicionários
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
# parametros: nome, saudacao
# retorno: string


def saudacoes(nome, saudacao='Oi'):
    return f'{saudacao} {nome} !'


print(saudacoes('João', 'Olá'))
print(saudacoes('Pedro'))
