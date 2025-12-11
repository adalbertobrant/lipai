""" Aula 03 - Tipos de Dados - Set ( Conjuntos ) """
# criar um set
numeros = {1, 2, 3, 4, 5, 6, 6.25, 6.5, 7, 8}
print(numeros, type(numeros))

# acesso dos elementos no set
for numero in numeros:
    print(numero)

# adicionar itens no set
numeros.add(100)
print(numeros)

# se adicionar um item que já existe no set
# apesar de rodar o programa ele não é adicionado
numeros.add(100)
print(numeros)
print('------')
# adicionar elementos de um set em outro
print(numeros)
numeros2 = {42, 3, 1, 11, 17}
print(numeros2)
numeros.update(numeros2)
print(numeros, type(numeros))
print('------')

# remove elementos de um set
numeros.remove(100)
print(numeros)

# copiando um set para outro
outro_set = numeros.copy()
print(outro_set)
