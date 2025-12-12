""" ex05.py: Implemente uma calculadora de Índice de Massa Corporal (IMC)
usando as diretrizes da OMS. Restante do enunciado na folha de exercícios entregue no teams
"""


def calcular_imc(individuo):
    """Retorna o IMC de um indivíduo com base na sua altura e peso."""
    altura, peso = individuo.values()
    return peso / (altura * altura)


def obter_classificacao(imc):
    """Retorna a classificação com base no IMC."""
    classificacao_imc = {
        (0.0, 18.4, 'Baixo peso'),
        (18.5, 24.9, 'Peso normal'),
        (25.0, 29.9, 'Excesso de peso'),
        (30.0, 34.9, 'Obesidade de Classe 1'),
        (35.0, 39.9, 'Obesidade de Classe 2'),
        (40.0, 999999999, 'Obesidade de Classe 3'),
    }
    for valor_inicial, valor_final, classificacao in classificacao_imc:
        if valor_inicial <= imc <= valor_final:
            return classificacao
    return None


def situacao_individuo(imc):
    """Retorna 'normal', 'perder peso' ou 'ganhar peso' usando dicionário de intervalos."""
    pesos = {
        (0.0, 18.4): 'ganhar peso',
        (18.5, 24.9): 'normal',
        (25.0, 999999999): 'perder peso',
    }

    for (minimo, maximo), indicacao in pesos.items():
        if minimo <= imc <= maximo:
            return indicacao
    return None


# Entrada de dados pelo usuário
altura = float(input('Digite a sua altura -> '))
peso = float(input('Digite o seu peso atual -> '))

pessoa = {
    'altura': altura,
    'peso': peso
}

imc = calcular_imc(pessoa)
classificacao_imc = obter_classificacao(imc)
situacao = situacao_individuo(imc)

print("  Calculadora IMC  ")
print()
print()
print(f'IMC = {pessoa['peso']} / {pessoa['altura']}²')
print(f'IMC -> {imc:.2f}')
print(f'Classificação IMC -> {classificacao_imc}')
print(f'Recomendações -> {situacao}')
