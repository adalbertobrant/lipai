""" Ex 02 - Carregar dados de projeto """


def carregar_dados_projetos(nome_arquivo):
    """Retorna uma tupla de dicionários com dados de projetos."""
    with open(nome_arquivo, 'r', encoding='utf-8') as arq:
        projeto = []
        for linha in arq:
            codigo, titulo, responsavel = linha.strip().replace('\'', '').split(',')
            projeto.append(
                {
                    'codigo': codigo,
                    'titulo': titulo,
                    'responsavel': responsavel
                }
            )

        return tuple(projeto)


ARQUIVO = 'arquivo_ex02.txt'

lista_dados = carregar_dados_projetos(ARQUIVO)

print(type(lista_dados))

print(lista_dados)
