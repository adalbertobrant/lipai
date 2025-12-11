""" Aula 05 - Tipos de dados """
# Numéricos
# int, float, complexos

IDADE = 20
PESO = 20.10
print(IDADE, type(IDADE))
print(PESO, type(PESO))

# String
NOME = 'JOAO'
SOBRENOME = 'SILVA'
NOME_COMPLETO = NOME + ' ' + SOBRENOME
print(NOME_COMPLETO)

# Interpolação de variáveis
PRODUTO = 'Coca-Cola'
print(f"{NOME} {SOBRENOME} comprou {PRODUTO}")

# Métodos em strings
# upper(), lower()
FRASE = 'TUDO ESTÁ ESCRITO EM MAIÚSCULA'
print(f"{FRASE.lower()}")
print(f"{FRASE.upper()}")

# separador no print
print(1, 2, 3, 4, 5, 6, sep=" / ")

# Boolean
LIGADO = True
print(LIGADO, type(LIGADO))

RESULTADO = 10 == 10
print(RESULTADO, type(RESULTADO))

# Listas

frutas = ['banana', 'manga', 'pera', 'maçã', 'laranja', 'abacaxi', 'limão']

print(f'{frutas}, tamanho da lista {len(frutas)}')

# adiciona elemento na lista
frutas.append('abacate')

# iteração sobre itens da lista
for fruta in frutas:
    print(fruta.upper())

# Tupla
codigos = ('spa1', 'spb1', 'spb3')
print(codigos[0])  # imprime o código que estiver na posição inicial da tupla
print(len(codigos))  # imprime o valor de elementos na tupla

# Set (Conjunto)
resultado_sorteio = {4, 5, 6, 7, 10}
print(resultado_sorteio)
resultado_sorteio.add(23)
print(resultado_sorteio)

# Dicionários (dictionary)
funcionario = {
    'codigo': 123,
    'nome': 'José da Silva',
    'salario': 7000.00
}

print(funcionario)
print(funcionario['codigo'])
print(funcionario['nome'])
print(funcionario['salario'])

print(funcionario.keys())  # mostra a lista de chaves
print(funcionario.values())  # mostra a lista de valores

# Alterando valores do dicionário
funcionario['salario'] = 9000.00
print(funcionario)
