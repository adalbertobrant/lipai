""" Ex 03 - Crie um programa que solicite um identificador ao usuário e
informe se é válido ou inválido
○ o código identificador contém 7 caracteres; 
○ começa com BR;
○ seguido de um número inteiro entre 0001 e 9999;
○ por fim, termina com o caractere X.
○ Exemplos válidos: BR0001X, BR1236X, BR9999X
○ Exemplos inválidos: br0001X, BR126X, BR99999X, BR9999Y """

identificador = input('Entre o identificador -> ')

tamanho_identificador = len(identificador) == 7

inicio_br = (identificador[0] == 'B' and identificador[1] == 'R')

# verifica se os números são válidos

QTD_INTEIROS = 4
SOMA_INTEIROS = 0

for i in range(2, 6):
    if identificador[i] in '0123456789':
        SOMA_INTEIROS += 1

NUMERO_VALIDO = False

if QTD_INTEIROS == SOMA_INTEIROS:
    meio = identificador[2:6]
    numero = int(meio)
    NUMERO_VALIDO = 1 <= numero <= 9999

x = identificador[-1] == 'X'

if tamanho_identificador and inicio_br and NUMERO_VALIDO and x:
    print(f'{identificador} é válido')
else:
    print(f'{identificador} não é válido')
