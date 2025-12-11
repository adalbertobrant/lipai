""" Aula 06 - Conversão de tipos """

# Conversão de tipo implícito ou explícito
LEITURA = 5.53
PESO = 3
TOTAL = LEITURA * PESO
print(TOTAL, type(TOTAL))  # fez a conversão implícita

# faz a convesão explícita (TYPE CASTING)
TOTAL = int(TOTAL)

print(TOTAL, type(TOTAL))

# Conversão para string

TEXTO = 'Maria tem ' + str(TOTAL) + ' unidades '
print(TEXTO, type(TEXTO))
