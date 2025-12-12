""" ex06.py: Crie um programa em Python que recebe como entrada o
comprimento, altura e largura (em cm) de um aquário e calcule:
○ O volume do aquário em litros;
○ A potência do termostato necessária para manter a temperatura adequada;
○ A quantidade de filtragem por hora (em litros) necessária para manter a
qualidade da água.
"""


def calcular_volume(medidas):
    """Calcula o volume do aquário em litros com base nas dimensões."""
    comp = medidas['comprimento']
    alt = medidas['altura']
    larg = medidas['largura']

    return (comp * alt * larg) / 1000


def calcular_potencia_termostato(volume, dados_aquario):
    """Calcula a potência do termostato baseada no volume e temperaturas."""
    temp_desejada = dados_aquario['temp_desejada']
    temp_ambiente = dados_aquario['temp_ambiente']

    return volume * 0.05 * (temp_desejada - temp_ambiente)


def calcular_filtragem(volume):
    """Retorna uma tupla com a filtragem mínima e máxima (2 a 3 vezes o volume)."""
    minima = volume * 2
    maxima = volume * 3
    return minima, maxima


# Entrada de dados pelo usuário
print("--- Dados do Aquário ---")
comprimento = float(input('Digite o comprimento (cm) -> '))
altura = float(input('Digite a altura (cm) -> '))
largura = float(input('Digite a largura (cm) -> '))
temp_ambiente = float(input('Digite a temperatura ambiente atual (°C) -> '))
temp_desejada = float(input('Digite a temperatura desejada (°C) -> '))


aquario = {
    'comprimento': comprimento,
    'altura': altura,
    'largura': largura,
    'temp_ambiente': temp_ambiente,
    'temp_desejada': temp_desejada
}

volume_litros = calcular_volume(aquario)
potencia = calcular_potencia_termostato(volume_litros, aquario)
filtragem_min, filtragem_max = calcular_filtragem(volume_litros)


print("\n  Resultados do Aquário  ")
print()
print(
    f'Dimensões ( Comprimento x Altura x Largura ) -> {aquario["comprimento"]}x{aquario["altura"]}x{aquario["largura"]}')
print(f'Volume do Aquário -> {volume_litros:.5f} Litros')
print(f'Potência do Termostato -> {potencia:.5f} W')
print(
    f'Filtragem Recomendada -> Entre {filtragem_min:.5f} e {filtragem_max:.5f} L/h')
