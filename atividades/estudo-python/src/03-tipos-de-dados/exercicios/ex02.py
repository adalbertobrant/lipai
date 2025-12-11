"""
ex02.py
○ Solicite ao usuário o mês do ano em formato numérico: 1, 2, 3, ..., 12.
○ Apresente o nome do mês correspondente (ex.: entrada 3 → saída
Março).
○ Implementar usando uma Tupla (tuple).
"""
mes_ano = int(input("Entre o mês do ano -> "))

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
if 1 <= mes_ano <= 12:
    print(meses[mes_ano - 1])
