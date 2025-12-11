""" Aula 05 - break e continue """

# Usa-se o break e continue dentro de um looping

for i in range(0, 10, 1):
    if i == 4:
        print('saída do loop')
        break
    print(i)

# encontrar a posição de um número
# em uma lista de inteiros. Caso não
# encontre posição i é igual a -1

busca = 5
numeros = [1, 33, 51, 6, 5, 7, 8, 9, 5, 1, 7]
posicao = -1
contador = 0

for numero in numeros:
    if numero == busca:
        posicao = contador
        print(f"Achei {busca} na posicao {posicao}")
    contador += 1

# usando o break para achar a primeira posicao
print("Usando o break para cancelar a execução do laço for")
busca = 5
numeros = [1, 33, 51, 6, 5, 7, 8, 9, 5, 1, 7]
posicao = -1
contador = 0

for numero in numeros:
    if numero == busca:
        posicao = contador
        print(f"Achei {busca} na posicao {posicao}")
        print('Saindo do for')
        break
    contador += 1

# exemplo com o range
print("Usando o range e o break no laço for")

busca = 5
numeros = [1, 33, 51, 6, 5, 7, 8, 9, 5, 1, 7]
posicao = -1

for i in range(len(numeros)):
    print('Procurando ... ...')
    if numeros[i] == busca:
        posicao = i
        break
print(f'{busca} encontrada na posicao {posicao}')


# Funcionamento do continue
# Apenas pula a iteração atual indo para a próxima iteração sem sair do looṕ

numeros = [1, 33, 513, 3, 3, 3, 3, 3, 3, 6, 5,
           7, 8, 9, 5, 1, 7, 3, 3, 3, 3, 3, 3, 3, 333]
for numero in numeros:
    if numero == 3:
        continue  # para a iteração atual do loop e vai para a próxima
    print(numero)
