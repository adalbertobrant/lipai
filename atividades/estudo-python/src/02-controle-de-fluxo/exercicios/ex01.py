""" Ex 01 - Solicite ao usuário 3 notas e apresente o 
resultado da média aritmética """

nota1 = float(input('Entre a nota 1-> '))
nota2 = float(input('Entre a nota 2-> '))
nota3 = float(input('Entre a nota 3-> '))

media = nota1 + nota2 + nota3
media = media / 3.0

print(f"Resultado da média das notas {nota1, nota2, nota3} é {media}")
