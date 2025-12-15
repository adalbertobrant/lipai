""" Aula 01 - Debug """


def somar(n1, n2, n3):
    """ retorna a soma das notas """
    soma = n1 + n2 + n3
    return soma


def calcular_media(n1, n2, n3):
    """ calcula a média das notas """
    soma = somar(n1, n2, n3)
    mean = soma / 3
    return mean


# breakpoint() #instrução de parada no código, vai para a linha 19 e espera comandos no terminal Pdb (python debuger)

NOTA1 = 10.0
NOTA2 = 3.0
NOTA3 = 5.5

breakpoint()
media = calcular_media(NOTA1, NOTA2, NOTA3)

print(media)
