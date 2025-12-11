"""
ex03.py
○ Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.
○ Apresente o nome do mês correspondente (ex.: entrada 3 → saída
Março).
○ Implementar usando um Dicionário (dict).
"""
mes_ano = int(input("Entre o mês do ano -> "))


meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}
if 1 <= mes_ano <= 12:
    if mes_ano in meses:
        print(meses[mes_ano])
else:
    print("Entre um mês de 1 a 12 apenas")
