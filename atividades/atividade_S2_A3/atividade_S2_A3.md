# Atividade S2 A3

**Nome**: Adalberto Caldeira Brant Filho

**Repositório GitHub**: https://github.com/adalbertobrant/lipai

# Código das Videoaulas

## Aula 01 - Tipos de Dados - Listas

  As listas podem ser:

     * ordenadas --> aceitam ordenação
     + mutáveis --> os elementos da lista podem ser editados ou terem seus valores alterados, com inclusão ou exclusão
     - indexáveis --> podem ser acessados através de um indice

```python3
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
```

## Aula 02 -Tipos de Dados - Tuplas

  Tuplas são conjuntos de elementos que são ordenadas e tem diferenças em relação as listas por serem imutáveis
  As tuplas são:
     + ordenadas
     + imutáveis
     + indexáveis

```python3
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

```
