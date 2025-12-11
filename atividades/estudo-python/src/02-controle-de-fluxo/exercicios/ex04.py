"""
Ex 04 - Baseado no ex03.py, apresente todas as inconsistências 
do identificador informado usando uma lista de erros.
"""

identificador = input('Entre o identificador -> ')

erros = []

if len(identificador) != 7:
    erros.append('O identificador não possui exatamente 7 caracteres.')

if len(identificador) >= 2:
    if not (identificador[0] == 'B' and identificador[1] == 'R'):
        erros.append('O identificador não inicia com a sequência BR.')
else:
    erros.append('O identificador não inicia com a sequência BR.')

if len(identificador) >= 6:
    QTD_INTEIROS = 4
    SOMA_INTEIROS = 0

    for i in range(2, 6):
        if identificador[i] in '0123456789':
            SOMA_INTEIROS += 1

    if QTD_INTEIROS == SOMA_INTEIROS:
        meio = identificador[2:6]
        numero = int(meio)
        if not (1 <= numero <= 9999):
            erros.append(
                'O identificador não apresenta número inteiro entre 0001 e 9999.')
    else:
        erros.append(
            'O identificador não apresenta número inteiro entre 0001 e 9999.')
else:
    erros.append(
        'O identificador não apresenta número inteiro entre 0001 e 9999.')

if len(identificador) >= 1:
    if identificador[-1] != 'X':
        erros.append('O identificador não finaliza com o caractere X.')
else:
    erros.append('O identificador não finaliza com o caractere X.')

print()
if len(erros) == 0:
    print(f'{identificador} é válido')
else:
    print(f'{identificador} não é válido')
    print('\nErros:')
    for erro in erros:
        print(f'# {erro}')
