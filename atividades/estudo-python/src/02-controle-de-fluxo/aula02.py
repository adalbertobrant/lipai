""" Aula 02 - instrução if """

# python usa identação
# if condição:
#     instrucao()
#     instrucao()
#     instrucao()

# outras linguagens c, java, c++

# if(){
#   instrucao()
#   instrucao()
#  }

codigo_cliente = 32
valor_desconto = 30.0
DESCONTO_ESPECIAL = valor_desconto >= 20.0

if DESCONTO_ESPECIAL:
    print('Desconto Especial')
    print(codigo_cliente)
else:
    print('Sem desconto especial')

# atenção com os cuidados com a identação pois pode ocorrer falhas, segundo a pep8 em sitaução de blocos deve-se usar 4 espaços

# regra do nome pelo menos 3 caracteres
nome = 'Lo'
print(len(nome))  # devolve 2

nome = 'Lois'
print(len(nome))  # devolve 4

if len(nome) < 5:
    print('Nome deve ter pelo menos 6 caracteres')
else:
    print('Nome válido')

NOME_INVALIDO = len(nome) < 3

if NOME_INVALIDO:
    print('Nome deve ter pelo menos 3 caracteres')
else:
    print('Nome válido')

NOME_VALIDO = len(nome) >= 3
if NOME_VALIDO:
    print('Nome válido')
else:
    print('Nome deve ter pelo menos 3 caracteres')

# regra do nome pelo menos 3 caracteres
# idade tem que ser maior ou igual a 18
# exibir todos os erros no final apenas
nome = 'Lo'
idade = 17
erros = []

NOME_INVALIDO = len(nome) < 3
if NOME_INVALIDO:
    erros.append('Nome deve ter pelo menos 3 caracteres')

IDADE_INVALIDADE = idade < 18
if IDADE_INVALIDADE:
    erros.append('Idade deve ser maior ou igual a 18')

if len(erros) != 0:
    print(erros)
else:
    print('Dados válidos')

# Dentro do if é avaliado como False as seguintes estruturas:
""" False, None, 0 , 0.0, string vazia '', lista, tuple, set vazio """
# Todo o resto é considerado dentro do if como True

# estrutura if elif else

# Verifica se um número é positivo,negativo ou zero

numero = 3

if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')


numero = 0

if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')

numero = -4

if numero > 0:
    print('Maior que zero')
elif numero == 0:
    print('Zero')
else:
    print('Menor que zero')

# faixas de valores devemos tentar particionar para 3 condições
# calcule a média e verifique se as duas notas são válidas antes do cálculo

n1 = 5
n2 = 10.0

NOTA1_VALIDA = 0 < n1 <= 10.0
NOTA2_VALIDA = 0 < n2 <= 10.0

if NOTA1_VALIDA and NOTA2_VALIDA:
    media = (n1 + n2) / 2.0

    if media >= 6.0:
        print('Aprovado')
    elif media >= 4.0:
        print('Recuperação')
    else:
        print('Reprovado')
else:
    print('Notas inválidas')
