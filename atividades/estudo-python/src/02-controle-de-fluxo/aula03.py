""" Aula 03 - loop for """

linguagens = ['C', 'Java', 'Python']
print(linguagens[0])
print(linguagens[1])
print(linguagens[2])

# loop for ajuda na iteração

# Sintaxe
# for valor in colecao:
#    instrucao
#    instrucao
#    instrucao

# nessa construção do for valor in colecao , o operador in , verifica se o elemento está dentro da coleção , retira e coloca no valor

# imprime cada linguagem em uma linha
for linguagem in linguagens:
    print(linguagem.upper())

# contar elementos e calcular a média

nota1 = 10.0
nota2 = 5.5
nota3 = 8.3

media = (nota1 + nota2 + nota3) / 3
print(media)

# em casos que temos uma lista o for ajuda
soma = 0
notas = [10, 9, 6, 7, 8, 10]
for nota in notas:
    soma = soma + nota
media = soma / len(notas)

# range em python

valores = range(0, 10)  # vai de zero até 9 pois o 10 não entra

for valor in valores:
    print(valor)

# steps in range

valores = range(0, 11, 2)  # vai de 2 em dois até o 10

# steps com decremento  in range

valores = range(10, 0, -1)  # 10, 9 , 8
print(valores)
for i in valores:
    print(i)


valores = range(10, -1, -2)  # 9, 7, 5, 3, 1
print(valores)
for i in valores:
    print(i)

for i in range(len(linguagens)):
    print(linguagens[i])

# o range é mais utilizado em casos em que não iremos percorrer de maneira linear a nossa coleção
