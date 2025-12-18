""" Ex 03 - Convertendo uma linha em dicionário genérico """


def linha_para_dict(frase, lista_chaves):
    """Recebe uma linha e uma lista de chaves e retorna um dicionário."""
    # cria uma lista com separador na vírgula para cada elemento da lista
    lista_linha = frase.strip().replace("'", "").split(',')
    if len(lista_linha) != len(lista_chaves):
        return f"{frase} e {lista_chaves} devem ter a mesma quantidade de itens"
    else:
        dicionario = {}
        for i in range(len(lista_chaves)):
            key = lista_chaves[i]
            valor = lista_linha[i]
            dicionario[key] = valor

        return dicionario


# casos testes

# caso teste 1
LINHA = "SP000001,Maria da Silva,maria@email.com"
chaves = ['prontuario', 'nome', 'email']
print(linha_para_dict(LINHA, chaves))

# caso teste 2
LINHA2 = "banana,3"
chaves2 = ['item', 'quantidade']
print(linha_para_dict(LINHA2, chaves2))

# caso teste 3
TEXTO = 'pentium IV, 8gb, 120gb,  False'
itens = ['cpu', 'memoria', 'hd', 'cd-room']
print(linha_para_dict(TEXTO, itens))

# caso teste 4
DATA = 'FM 104.5, canal 8, faixa cidadão'
dados = ['radio', 'tv']
print(linha_para_dict(DATA, dados))
