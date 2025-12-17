""" Aula 02 - Manipulação arquivos python """

# abrindo um arquivo
arq = open('arquivo_.txt', 'w', encoding='utf-8')
# imprime o conteúdo
print(arq)
# escreve no arquivo uma string
arq.write('escreve uma única string\nque pode ser barra n \n')
# iterável de strings para gravação usando o writelines()
lista = ['nom', 'nome', 'nomer', 'homer']
arq.writelines(lista)

# forma mais correta de abrir arquivos em python
with open('arquivo_texto.txt', 'w', encoding='utf-8') as arq:
    arq.write('teste\ntestando\ntestador\n')

# ao sair da subrotina with open, temos que o arquivo aberto para leitura já está fechado

# modo append
with open('arquivo_texto.txt', 'a', encoding='utf-8') as arq:
    arq.write('adicionando linha no final do arquivo')

# modo leitura
with open('arquivo_texto.txt', 'r', encoding='utf-8') as arq:
    x = arq.read()
    print(x)
    print(type(x))
    # ir para o início do arquivo
    arq.seek(0)
    # lê o arq e transforma em uma lista
    x = arq.readlines()
    print(x)
    print(type(x))

# leitura modo binário (rb)
with open('arquivo_texto.txt', 'rb') as arq:
    x = arq.read()
    print(x)
    print(type(x))
    # para decodificar de binário para string podemos usar o método decode()
    print(x.decode())
    print(type(x.decode()))

# gerador iterável arq
with open('arquivo_texto.txt', 'r', encoding='utf-8') as arq:
    for i in arq:
        print(i)
