""" Aula 02 - Tipos de Dados - Tuplas """

# criação da tupla

nomes = ('Maria', 'Pedro', 'João')
print(nomes, type(nomes))

# acessar os elementos da tupla da mesma forma que acessa em uma lista
print(nomes[0])
print(nomes[0:3])
print(nomes[-1])

# a leitura de dados na tupla e lista são iguais
# a tupla não aceita modificação de valores

# iteração em tuplas é igual a de listas
for nome in nomes:
    print(nome)

# outra forma de criar tuplas

nomes2 = 'ana', 'amelia', 'marcos'
print(nomes2, type(nomes2))

# unpack - atribuir para variáveis os valores que estão na tupla
nome1 = nomes[0]
nome2 = nomes[1]
nome3 = nomes[2]

# usando o unpack temos:
nome1, nome2, nome3 = nomes
# o unpack deve ser igual a quantidade de elementos da tupla ou o seu fatiamento
nome1, nome2 = nomes[0:2]  # unpack fatiado
print(nome1, nome2)

# juntas duas tuplas

todos_nomes = nomes + nomes2
print(todos_nomes)

# para escolher entre listas e tuplas , avaliar os dados se imutáveis preferir usar tupla
