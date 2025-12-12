""" Aula 03 - Python: entendendo o uso de *args e **kwargs em funções e métodos """

# *args
# o nome args vem de argumentos no plural pois podem ser vários
# o *args funciona como uma lista


def compras(nome_supermercado, *lista_compras):
    print(f'Ir no -> {nome_supermercado}')
    for produtos in lista_compras:
        print(f'Comprar -> {produtos}')


super = 'Mercadinho de Casa'
comprar = ['sabão em pó - OMO',
           'sabão de barra -ypê',
           'detergente - limpol',
           'palha de aço - BomBril',
           ]
# ao passar os dois argumentos da função sem usar o *comprar
# observamos que a lista comprar é entendida como apenas um único elemento
compras(super, comprar)
print()
print()
print("    FORMA CORRETA USANDO *comprar   ")
print()
# passar a lista comprar utilizando a forma *args -> *comprar
# o programa funciona da forma esperada
compras(super, *comprar)

# **kwargs
# O **kwargs no python é conhecido como keyword arguments, ou seja é necessário
# passar uma chave e um valor para utilizar esse argumento
# Dada a situação de que clientes tem desconto de 10% , funcionários tem desconto de 30%
# devedores não tem desconto e devem pagar apenas no dinheiro
# e o dono leva de graça os produtos do supermercado
# como criar o **kwards dessa situação ?

def calcular_preco(preco, **kwargs):
    descontos = {
        'cliente': 0.10,
        'funcionario': 0.30,
        'dono': 1.0
    }
    desconto = 0

    for tipo, valor in kwargs.items():
        if tipo in descontos:
            desconto = descontos[tipo]
            break

    # Calcular o preço final com desconto
    preco_final = preco * (1 - desconto)

    # Verificar condição de pagamento para devedores
    if kwargs.get('devedor', False):
        print("Tem dívida - Pagar em dinheiro apenas!")
        return preco  # Sem desconto para devedores

    return preco_final


# Dicionário de pessoas
pessoas = {
    'maria': {
        'nome': 'Maria Silva',
        'idade': 35,
        'cliente': True
    },
    'jose': {
        'nome': 'José Santos',
        'idade': 45,
        'funcionario': True
    },
    'pedro': {
        'nome': 'Pedro Oliveira',
        'idade': 50,
        'dono': True
    },
    'ana': {
        'nome': 'Ana Souza',
        'idade': 28,
        'devedor': True
    }
}

preco_produto = 100.0

for pessoa, detalhes in pessoas.items():
    print(f"\nNome: {detalhes['nome']}")
    print(f"Preço original: R$ {preco_produto:.2f}")

    # Passar os kwargs dinamicamente
    preco_final = calcular_preco(
        preco_produto, **{k: v for k, v in detalhes.items()
                          if k != 'nome' and k != 'idade'})

    print(f"Preço final: R$ {preco_final:.2f}")
