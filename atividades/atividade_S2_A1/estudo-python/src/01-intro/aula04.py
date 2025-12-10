""" Aula 04 - Variáveis , Constantes e Literais """
# variável é um container para guardar dados
# inferência do tipo
numero = 10
print(numero, type(numero))

# multiplas atribuições
maria, idade, endereco = "Maria", 20, "Rua 10 numero 1"
print(f"Nome-> {maria}, Idade-> {idade}, Endereço-> {endereco}")

nome1 = nome2 = nome3 = "João"
print(nome1, nome2, nome3)
nome2 = "Pedro"
print(nome1, nome2, nome3)

# snake_case
# idfuncionario = 49
id_funcionario = 49
salario_atual = 200
print(id_funcionario, salario_atual)

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
nomes = {'maria', 'maria', 'joao', 'pedro', 'maria', 'Pedro'}
print(nomes, type(nomes))

# Dicionário (dictionary)
aluno = {
    'prontuario': 1234,
    'nome': 'Maria da Silva',
    'idade': 34
}
print(aluno, type(aluno))
    