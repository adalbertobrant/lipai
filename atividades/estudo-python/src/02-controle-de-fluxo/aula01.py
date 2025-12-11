#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Aula 01 - Operadores """

n1 = 10.2
n2 = 3.5
resultado = n1 + n2 + 8.5

# Operadores Aritméticos
print('1 + 1', 1 + 1, type(1 + 1))
print('1.5 + 1.7', 1.5 + 1.7, type(1.5 + 1.7))
print('resultado ', resultado, type(resultado))
print(3-1)
print(3*2, type(3*2))
print(3/2, type(3/2))
print(3 % 2, type(3 % 2))
print(10 // 3, type(10 // 3))
print(10 ** 2, type(10 ** 2))

# Operador de atribuição
x = 10.0
print(x, type(x))

# Operadores de comparação ou relacionais
if x > 10:
    print(True)

resultado = x == 10
print(resultado, type(resultado))

print('10 == 10', 10 == 10, type(10 == 10))
print('10 != 10', 10 != 10, type(10 != 10))
print('10 > 10', 10 > 10, type(10 > 10))
print('10 >= 10', 10 >= 10, type(10 >= 10))
print('10 < 10', 10 < 10, type(10 < 10))
print('10 <= 10', 10 <= 10, type(10 <= 10))

condicao = x > 10 and resultado < 3

if condicao:
    pass

# Operadores lógicos
# and
print('True and True ->', True and True, type(True and True))
print('True and False ->', True and False, type(True and False))
print('False and True ->', False and True, type(False and True))
print('False and False ->', False and False, type(False and False))

# or
print('True or True', True or True, type(True or True))
print('True or False', True or False, type(True or False))
print('False or True', False or True, type(False or True))
print('False or False', False or False, type(False or False))

# not
condicao = True
print('not condicao', not condicao, type(not condicao))

condicao = False
print('not condicao', not condicao, type(not condicao))

# Operadores especiais

# is
# == compara se dois valores são iguais
# is verifica se as variáveis apontam para o mesmo objeto em memória
a = 10
b = 10.0
c = b

print(a == b, a == c, b == c)
print(a is b, a is c, b is c)

# in
# devolve um booleano
# pode ser usado com str, list, tuple, set, dic (apenas na chave)

frase = 'o rato roeu'
print('o' in frase, type('o' in frase))
print('O' in frase, type('O' in frase))

# in in listas
numeros = [1, 3, 5, 7, 11, 2]
print(0 in numeros)
print(-2 in numeros)
print(11 in numeros)

# in in tuplas
numeros = (0, 1, 2, 3, 4, 5, 6, 7, 10)
print(100 in numeros)
print(2 in numeros)

# in in sets
numeros = {1, 2, 34, 5, 7}
print('' in numeros)
print(2 in numeros)

# in in dicionários , apenas busca na chave e não no valor
pessoa = {
    'nome': 'José da Silva',
    'idade': 22,
    'email': 'jose@mail.com'
}

print('nome' in pessoa)  # True
print('José da Silva' in pessoa)  # False
print('email' in pessoa)  # True
print('jose@mail.com' in pessoa)  # False
