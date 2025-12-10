""" Aula 04 - Variáveis , Constantes e Literais """
# variável é um container para guardar dados
# inferência do tipo
NUMERO = 10
print(NUMERO, type(NUMERO))

# multiplas atribuições
maria, idade, endereco = "Maria", 20, "Rua 10 numero 1"
print(f"Nome-> {maria}, Idade-> {idade}, Endereço-> {endereco}")

NOME1 = NOME2 = NOME3 = "João"
print(NOME1, NOME2, NOME3)
NOME2 = "Pedro"
print(NOME1, NOME2, NOME3)

# snake_case
# idfuncionario = 49
ID_FUNCIONARIO = 49
SALARIO_ATUAL = 200
print(ID_FUNCIONARIO, SALARIO_ATUAL)

# Constantes
# Upper case - snake_case
MAIORIDADE_CIVIL = 21
MAIORIDADE_PENAL = 18
print(MAIORIDADE_CIVIL, MAIORIDADE_PENAL)

# literais
print(27)  # 27 é o literal
IDADE = 27
print(IDADE, type(IDADE))  # type mostra o tipo da variável ou do literal

# Strings
NOME = "Maria da Silva"
print(maria, type(maria))

# Booleano
print(True, type(True))
print(False, type(False))

# None
print(None, type(None))

# Coleções

# Lista
numeros = [1, 2, 3]
print(numeros, type(numeros))

# Tupla(tuple)
emails = ('joao@mail.com', 'maria@mail.com')
print(emails, type(emails))

# Conjunto (set)
# nomes = {'maria', 'maria', 'joao', 'pedro', 'maria', 'Pedro'}
nomes = {'maria', 'joão', 'pedro'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'prontuario': 1234,
    'nome': 'Maria da Silva',
    'idade': 34
}
print(aluno, type(aluno))
