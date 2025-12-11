""" Aula 04 - Loop while """

# Repetir instruções quando não temos uma instrução ou condição clara antes de verificar valores inicialmente
# Quando uma lista não está completamente na memória ainda, ou seja está em construção dinâmica
# muito usado em leitura de arquivos , em leitura com cursores

# while condição_for_verdadeira:
#    instrução
#    instrução
#    instrução

contador = 0

while contador <= 10:
    print(contador)
    contador += 1  # incremento da condição
print('fim')

# exemplo de leituras em arquivo
# arquivo já está aberto
"""
linha = arquivo.readline()
while linha:
    instrucao_linha
    linha = arquivo.readline()  # vai ler até encontrar uma linha final
"""

# O while funciona pelo mesmo princípio de condição ou seja ele precisa de uma condição verdadeira para entrar em seu laço, sendo condições False a razão de saída do laço while
