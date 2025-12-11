"""" Aula 01 - Introdução a funções """

# funções built-in functions

nome = 'José'
print(nome)
print(len(nome))

# User Defined Functions
# são definidas pelo usuário do programa python
# fazem parte da solução do problema

# função saudacoes


def saudacoes():
    print("Hello World")


# para imprimir o resultado da função saudacoes, deve-se chamar a função
saudacoes()
saudacoes()

# imprime saudacao com nome


def ola(nome):
    print(f'Olá, {nome}')


# maria é o argumento do parametro nome
ola('Maria')

# função para calcular a media


def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3)/3
    print(media)


# chamada
# argumentos são literais
calcular_media(10, 5, 7)

n1 = 5
n2 = 7
n3 = 8

# chamada
# argumentos são variáveis
calcular_media(n1, n2, n3)

# Declaração
# nome: media
# parametros: nota1, nota2, nota3
# retorno: media


def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3)/3.0


media = media(10, 7, 4)
print(f'Valor da média é {media}')

# quando colocamos um retorno na função ele pode ser usado em diferentes cenários, como salvar em um banco de dados, enviar um email , salvar em um arquivo
