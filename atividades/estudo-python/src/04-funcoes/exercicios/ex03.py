""" ex03.py: Crie uma função que recebe uma tupla de números como
parâmetro (numeros) e retorna a soma desses números """


def soma_tuplas(tuplas_numeros=()):
    """ retorna a soma dos elementos da tupla """
    somador_tupla = 0
    for n in tuplas_numeros:
        somador_tupla += n

    return somador_tupla


tuplas = (1, 2, 3, 4, 5, 6, 9, 100, -23, -45, 10, -34)

print(
    f'  A soma dos números na tupla -> {tuplas}\n  É de {soma_tuplas(tuplas)}')
