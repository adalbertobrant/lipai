""" 
ex01.py
○ Solicite ao usuário 3 números.
○ Armazene os valores em uma lista.
○ Ao final, apresente o menor e o maior elemento.

"""
lista = []
CONTADOR = 0
while CONTADOR < 3:
    lista.append(int(input('Entre um valor para a lista -> ')))
    CONTADOR += 1

menor = maior = lista[0]

for x in lista:
    if x < menor:
        menor = x
    if x > maior:
        maior = x

print(f'O menor valor da lista {lista} é {menor}')

print(f'O maior valor da lista {lista} é {maior}')
