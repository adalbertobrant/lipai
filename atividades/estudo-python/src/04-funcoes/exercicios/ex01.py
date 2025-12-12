""" ex01.py: Crie uma função que recebe três números 
como parâmetro (n1, n2,n3) e imprime na saída padrão a soma dos números."""

# declaração: função soma
# recebe 3 números como parâmetros
# returna a soma dos 3 números


def soma(n1, n2, n3):
    """ soma de 3 números """
    print(n1 + n2 + n3, sep="")


print('Soma de 1,2,3 -> ', end="")
soma(1, 2, 3)

print('Soma de n2 = 2,n1 = 0,n3 = 4* 5 -> ', end="")
soma(n2=2, n1=0, n3=4*5)

N1 = 10
N2 = 1
N3 = 2

print('Soma de N1 = 10, N2 = 1 = N3 = 2 -> ', end="")
soma(N1, N2, N3)
