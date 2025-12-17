""" Aula 01 - Manipulação de Arquivos """

# importando biblioteca para exclusão de arquivos
import os

# abertura do arquivo

arquivo = open("teste.txt", "r", encoding='utf-8')

# verifica se o arquivo tem condições de ser lido
print(arquivo.readable())

# função read(), retorna todo o arquivo lido
print(f'\nRetorna o arquivo lido abaixo:\n{arquivo.read()}')

# função para retornar o cursor de leitura para o início do arquivo
arquivo.seek(0)

# ler um arquivo linha a linha
primeira_linha = arquivo.readline()
print(f'\nLeitura do arquivo na primeira linha -> {primeira_linha}')

# voltar o arquivo para o início do arquivo
arquivo.seek(0)

# lendo várias linhas ao mesmo tempo e guardando em uma lista

lista_arquivo = arquivo.readlines()

# imprime a lista
print(f'\n\nImprime a lista \n{lista_arquivo}')

# fechar o arquivo
arquivo.close()

# abrir o arquivo para modo de adicionar no final append

arquivo = open("teste.txt", "a", encoding='utf-8')

# adicionar texto
ADICIONAR_TEXTO = '\nC\nRust\n'  # pois o anterior estava na mesma linha

# verificar se o arquivo aceita escrita
if arquivo.writable():
    # adicionar texto no arquivo
    arquivo.write(ADICIONAR_TEXTO)
    arquivo.close()

# abrindo novamente o arquivo agora no modo leitura
arquivo = open('teste.txt', 'r', encoding='utf-8')

# variável lista recebe lista do conteúdo de arquivo
lista = arquivo.readlines()

# imprimir lista
print(f'\nNova lista gerada\n{lista}')

# fechar o arquivo
arquivo.close()

# removendo arquivo
# os.remove('teste_arquivo.txt')

# verificando se o arquivo pode ser removido ou não
if os.path.exists('teste_arquivo.txt'):
    os.remove('teste_arquivo.txt')
else:
    print('Arquivo não existe')

# removendo uma pasta
os.rmdir('src/06-arquivos/nova_pasta')
