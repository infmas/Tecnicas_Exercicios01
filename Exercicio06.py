""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 06
"""

from datetime import datetime

def ValidaIdade(idade):
    try:
        idadeValidada = int(idade)
        if idadeValidada <= 0 or idadeValidada > 150:
            idadeValidada = -1   #indica idade inválida
    except ValueError:
        idadeValidada = -2   #indica número inválido
    return idadeValidada

nome = input("Informe seu nome: ")
idade = ValidaIdade(input("Informe sua idade (anos): "))
if idade < 0:
    if idade==-1:
        print("Idade deve ser em anos entre 1 e 150.")
    elif idade==-2:
        print("Idade informada inválida.")
    quit()

now = datetime.now()
anoNascimento = now.year - idade
ano100anos = anoNascimento + 100

if idade == 100:
    print(f"Atualmente você tem 100 anos, no ano {now.year}")
elif idade > 100:
    print (f"{nome}, você teve 100 anos no ano {ano100anos}")
elif idade < 100:
    print (f"{nome}, você terá 100 anos no ano {ano100anos}")