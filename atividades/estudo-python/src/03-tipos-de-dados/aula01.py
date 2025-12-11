"""" Aula 01 - Tipos de Dados - Listas """

# exemplo lista vazia
nomes = []
print(nomes, type(nomes))

nomes = ['josé', 'maria', 'pedro', 'paulo', 'marcos']
print(nomes, type(nomes))

# permite adicionar tipos diferentes
coisas = ['panela', 2, 1.614, ['outra_lista', 'coisas'], 100]
print(coisas, type(coisas))

# permite acessar elementos através de um indice
print(coisas[0])
print(coisas[0:3])
print(coisas[-1])
print(coisas[:2])
print(coisas[3:6])

# modificação de elementos na lista

lista_nomes = ['Maria', 'Marta', 'Ana', 'Priscila', 'Raquel']
print(lista_nomes[0])
lista_nomes[3:] = ['Pedro', 'João']
print(lista_nomes)

# tamanho de uma lista
print(len(lista_nomes))

# adicionar elementos na lista usando o append

nomes = []
nomes.append('Josefo')
nomes.append('Marta Gomes')

# insere um elemento em posição específica
# o insert desloca os elementos e adiciona elementos de acordo com o indice passado

nomes.insert(0, 'Guilherme Tavares')
print(nomes)

# método extend - acrescenta uma lista em outra lista no final da mesma
nomes2 = ['carlos gomes', 'caio silva']
nomes.extend(nomes2)
print(nomes)

# remover elementos da lista - passando o elemento a ser removido
# deve ser usado sempre com tratamento de erros
print(nomes)
nomes.remove('carlos gomes')
print(nomes)

# del - deleta nomes passando o indice, remove da memória
print(nomes)
del nomes[0]
print(nomes)
# se usar del nomes apenas , irá apagar a variável da memória

# limpar o conteúdo da lista deixando ela vazia
print(f'Lista nomes -> {nomes}')
nomes.clear()  # limpa elementos da lista (todos)
print(nomes)

# iteração em listas
for nome in lista_nomes:
    print(nome)

for i in range(len(lista_nomes)):
    print(lista_nomes[i])
