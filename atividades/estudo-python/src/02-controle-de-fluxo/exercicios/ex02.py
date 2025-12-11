""" Ex02 - Solicite ao usuário, uma única vez, as notas no formato n1, n2, n3,
nm e apresente:a média aritmética das notas;
○ a situação: aprovado (média > 6.0), recuperação (4.0 ≤ média ≤ 6.0) ou
reprovado (média < 4.0)."""

lista_notas = input("Entre todas as notas separadas por ';' -> ")

lista_notas = lista_notas.split(sep=';')

lista_notas = [float(nota.strip()) for nota in lista_notas if nota.strip()]

media = sum(lista_notas) / len(lista_notas)

print(f'Média das notas -> {media}')

if media > 6.0:
    print('Aprovado')
if media >= 4.0 and media <= 6.0:
    print('Recuperação')
if media < 4.0:
    print('Reprovado')
