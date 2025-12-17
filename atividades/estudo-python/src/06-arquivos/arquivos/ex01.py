""" Ex 01 - Carregar dados de alunos """


def carregar_dados_alunos(nome_arquivo):
    """ retorna uma tupla de dicionários com os dados do arquivo """
    lista_dicionario = list()
    with open(nome_arquivo, 'r', encoding='utf-8') as arq:
        linha = arq.read()
        linha = linha.split('\n')
        for i in range(len(linha)):
            prontuario, nome, email = linha[i].split(',')
            lista_dicionario.append(
                {
                    'prontuario': prontuario,
                    'nome': nome,
                    'email': email
                }
            )

    return tuple(lista_dicionario)


ARQUIVO = 'arquivo_ex01.txt'

lista_dados = carregar_dados_alunos(ARQUIVO)

print(type(lista_dados))

print(lista_dados)
