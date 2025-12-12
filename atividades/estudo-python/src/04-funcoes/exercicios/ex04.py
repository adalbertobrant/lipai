""" ex04.py: Crie uma função que recebe vários argumentos numéricos através
de *args e retorna a soma dos números. """


def soma_args(*args):
    """ retorna a soma de uma lista de números """
    soma = 0
    for n in args:
        soma += n
    return soma


lista_numeros = [1.1, 2.5, 6.7, 3, 45, 100, -93,
                 98, -100.95, 33, 52.99, -100.76, 30]

print(
    f'A soma da lista de números -> {lista_numeros}\nÉ {soma_args(*lista_numeros)}')
