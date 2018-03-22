""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 01
"""

numero1 = input("Insira o primeiro número: ")
try:
    numero1=float(numero1)
except ValueError:
    print("Primeiro número informado é inválido.")
    quit()

numero2 = input("Insira o segundo número: ")
try:
    numero2=float(numero2)
except ValueError:
    print("Segundo número informado é inválido.")
    quit()

if float(numero1) > float(numero2):
    print (f"O primeiro número informado ({numero1}) é o maior.")
elif float(numero1) < float(numero2):
    print (f"O segundo número informado ({numero2}) é o maior.")
else:
    print (f"Os números informados são iguais.")