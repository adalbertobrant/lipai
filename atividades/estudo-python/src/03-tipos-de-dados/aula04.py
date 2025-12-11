""" Aula 04 - Tipos de Dados - Dicionário (dic) """
# criar um dicionário
carro = {
    'marca': 'ford',
    'modelo': 'mustang',
    'ano': 1964
}
print(carro, type(carro))

# acessar os valores de um dicionário
print(carro['marca'])
print(carro.get('marca'))

# pegar todas as chaves
print(carro.keys(), type(carro.keys()))  # retorna um conjunto de chaves

# pegar todos os valores
print(carro.values(), type(carro.values()))

# pegar todos os pares (chave:valor)
print(carro.items(), type(carro.items()))  # retorna conjunto de tuplas

# verifica se a chave existe
print("marca" in carro)
print("cor " in carro)

# adicionar chave/valor de forma dinâmica
carro['cor'] = 'azul'
print(carro)
print('cor' in carro)


# remover um item do dicionario através de sua chave
carro.pop('marca')
print(carro)

# o pop no dicionário retorna o valor removido
valor_removido = carro.pop('cor')
print(f'A cor {valor_removido} foi removida do dicionário{carro}')

# iterar com o dicionário
for key in carro:
    print(key, carro[key], type(key))

for key in carro.keys():
    print(key)

for value in carro.values():
    print(value)

for key, value in carro.items():
    print(key, value)

# lista de dicionários

aluno1 = {
    'nome': 'João',
    'email': 'joao@mail.com',
    'notas': [10, 7, 8]
}

aluno2 = {
    'nome': 'Maria',
    'email': 'maria@mail.com',
    'notas': [10, 5, 6]
}

alunos = [aluno1, aluno2]

for aluno in alunos:
    print(aluno['nome'], aluno['email'])
    for nota in aluno['notas']:
        print(nota)
