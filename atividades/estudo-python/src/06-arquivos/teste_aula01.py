""" teste para ver se o open funciona ao ter um arquivo já usando ele """
# abre arquivo para escrita
arquivo = open('teste_arquivo.txt', 'w', encoding='utf-8')

# escreve no arquivo
arquivo.write('Escrevendo algo no arquivo\n')

# testa se o arquivo pode ser lido
if arquivo.readable():
    print('O arquivo pode ser lido')
else:
    print('Arquivo não pode ser lido')

# tentativa de abrir o arquivo para leitura
arquivo_leitura = open('teste_arquivo.txt', 'r', encoding='utf-8')

# testa se o arquivo foi lido e aberto
if arquivo_leitura.readable():
    print(arquivo_leitura.readlines())
