""" Aula de Numpy - 01 """

import matplotlib.pyplot as plt
from time import process_time
from numpy.random import default_rng
import numpy as np

# criando um vetor no numpy
vetor = np.array([1, 2, 3, 4, 5, 6])
print(vetor)
print(vetor[0:3])
print(type(vetor))

# criando um array no numpy com zeros e dimensões ( x = 5, y = 3, z = 6 )
zeros_array = np.zeros(shape=(5, 3, 6))
print(zeros_array)

# criando um array no numpy com números um e dimensões ( x = 5, y = 3, z = 6 )
um_arrays = np.ones(shape=(5, 3, 6))
print(um_arrays)

# criando um array empty no numpy
vazio = np.empty((7, 6))
print(vazio)

# criando um array com np.arange([start, ]stop, [step, ]dtype=None, *, like=None)
arr = np.arange(10)  # cria um array com os valores de zero até 9
arr = np.arange(start=100, stop=0, step=-10)
print(arr)

# criando um array que segue uma lógica linear np.linspace()
array_linear = np.linspace(start=0, stop=100, num=20,
                           endpoint=False, retstep=True)
print(array_linear)

# descobrindo dados do array
print(zeros_array.shape)  # mostra as dimensões do array
print(zeros_array.size)  # mostra a quantidade de elementos do array
print(zeros_array.ndim)  # mostra a quantidade de dimensões do array

# mudando o tamanho de um array np.reshape ( array, shape, order {'C', 'F', 'A}, *, copy=None)
# na parte de order pode ter a leitura seguindo o padrão C -> último index é o de maior variação,
# Fortran -> primeiro index é o de maior variação
# A -> também é leitura fortran mas usando memória contígua

print(arr)
arr = arr.reshape((5, 2), order='F')
print(arr)

# Ranqueando um array np.sort( array, axis=-1, kind=None, order=None, *, stable=None )
# axis -1 -> usa o último eixo para fazer o ranque
# kind -> tipo de ordenação quicksort, mergesort, heapsort, timsort, stable
# order -> qual o campo deve ser utilizado para realizar a comparação
# stable -> se verdadeiro True devolve o array com sua ordem relativa
print('---')
arr = np.sort(arr, axis=1, kind='heapsort')
print(arr)

# transformando um vetor 1-D em uma matriz 2-D
# np.newaxis()
a = np.array([1, 2, 3, 4, 5])
print(a.ndim)
a2 = a[np.newaxis, :]
print(a2)

a2 = a[:, np.newaxis]
print(a2)

# acessando valores usa o mesmo prncípio de listas
print(a2[1][0])

# concatenando arrays np.concatenate()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

c = np.concatenate((a, b))
d = np.concatenate((b, a))

print(c)
print(d)

# consultando itens de um array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a)
print('-----')
pares = a[(a % 2 == 0) & ~(a > 5)]  # o and -> & , or -> | , not -> ~
print(pares)

print('------\nOperações com array\n-----')
# operações com arrays
a = np.array([[0, 1, 2, 3], [4, 5, 6, 6.5], [7, 8, 9, 11]])
# na soma os dados devem ser homogenos, se tiver um tamanho diferente , dará erro
print(f"Soma do array -> {a.sum()}")
print(f"Valor máximo no array -> {a.max()}")
print(f"Valor minimo no array -> {a.min()}")
print(f"Valor da média no array -> {a.mean()}")
print(f"Valor da mediana no array -> {np.median(a)}")

# Gerando amostras aleatórias no numpy
# from numpy.random import default_rng

rng = default_rng()
aleatorio = rng
print(aleatorio)
aleatorio = rng.integers(20, size=(3, 3, 2))
print(aleatorio)

# diferenças entre arrays do numpy e listas
# velocidade do array é maior
# array do numpy sempre trabalha com o mesmo tipo de dado, se tiver uma string no meio de ints, tudo será string

# comparando o processamento entre array numpy
# from time import process_time
print('----- Usando listas ----')
lista_a = list(rng.integers(10, 100, 10000000))
lista_b = list(rng.integers(10, 100, 10000000))
c = []
# c = lista_a * lista_b
# Traceback (most recent call last):
#  File "/home/adalberto/github/lipai/atividades/estudo-python/src/08-numpy/aula01.py", line 116, in <module>
#    c = lista_a * lista_b
#        ~~~~~~~~^~~~~~~~~
# TypeError: can't multiply sequence by non-int of type 'list'
t1 = process_time()
for i in range(len(lista_a)):
    c.append(lista_a[i] * lista_b[i])
t2 = process_time()
print(f"Tempo de processamento gasto -> {t2 - t1}")
print('----- Usando numpy ----')
a = rng.integers(10, 100, 10000000)
b = rng.integers(10, 100, 10000000)

t1 = process_time()
c = a * b
t2 = process_time()
print(f"Tempo de processamento gasto -> {t2 - t1}")

# gráficos com numpy
# import matplotlib.pyplot as plt
dados_x = rng.integers(20, size=30)
dados_y = rng.integers(12, size=30)

plt.scatter(x=dados_x, y=dados_y)

plt.show()
