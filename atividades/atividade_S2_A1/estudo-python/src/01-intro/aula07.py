""" Aula 07 - Entrada e Saída """

# alterando o sep e o end no python print()
print('hello world', 'Maria', True, 1, sep=" @ ", end=' !!!\n')
print('hello world', sep=' ### ', end='\n\n\n')

# Salvando o conteúdo do print dentro de um arquivo e fora da saída de tela padrão

arquivo = open('nome_arquivo.txt', 'w', encoding='utf-8')
print(f"{arquivo}", file=arquivo)
print(f"Saída de dados no arquivo -> {arquivo}",
      file=arquivo, sep=" %% ", end='\n\n')


# Entrada de dados em python

nome = input("Digite o seu nome -> ")
print(nome.upper())
idade = input("Digite a sua idade -> ")
print(idade, type(idade))
idade = int(input("Digite a sua idade -> "))
if idade >= 18:
    print(f"{nome} é maior de idade!!")
else:
    print(f"{nome} é menor de idade !!")

# File - Entrada de dados a partir de arquivos
arq = 'notas.txt'
escrever_arquivo = open(arq, 'w', encoding='utf-8')

nota1 = input("entre a nota1 do aluno de zero a dez -> ")
nota2 = input("entre a nota2 do aluno de zero a dez -> ")
nota3 = input("entra a nota3 do aluno de zero a dez -> ")

print(nota1, nota2, nota3, sep=";", file=escrever_arquivo)

# Deve-se fechar o arquivo
escrever_arquivo.close()

arquivo_notas = open(arq, 'r', encoding='utf-8')
conteudo = arquivo_notas.read()
print(conteudo)
print(conteudo.split(sep=';'))
notas = conteudo.split(sep=';')
media = (float(notas[0]) + float(notas[1]) + float(notas[2])) / len(notas)
print(media)

# Fechar o arquivo no final
arquivo_notas.close()
