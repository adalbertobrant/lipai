""" ex02.py: Crie uma função que recebe três números como parâmetro (n1, n2,
n3) e retorna a soma dos números."""


def somar_numeros(n1=0, n2=0, n3=0):
    """ retorna a soma dos números n1,n2,n3 """
    return n1+n2+n3


N1 = 100
N2 = 300
N3 = -190

print(f'A soma de {N1} + {N2} + {N3} -> {somar_numeros(n2=N2, n1=N1, n3=N3)}')
