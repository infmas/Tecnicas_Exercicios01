""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 03
"""

def ValidaNota(nota):
    try:
        notaValidada = float(nota)
        if notaValidada < 0 or notaValidada > 10:
            notaValidada = -1   #indica valor fora do range
    except ValueError:
        notaValidada = -2   #indica número inválido

    return notaValidada


numero1 = ValidaNota(input("Insira a primeira nota do aluno: "))
numero2 = ValidaNota(input("Insira a segunda nota do aluno: "))

if numero1 == -1:
    print("Valor da nota deve ser entre 0 e 10.")
elif numero1 == -2:
    print("Primeira nota informada é inválida.")

if numero2 == -1:
    print("Valor da nota deve ser entre 0 e 10.")
elif numero2 == -2:
    print("Segunda nota informada é inválida.")

if numero1 < 0 or numero2 < 0:
    quit()

media = (numero1 + numero2) / 2

if media < 7:
    print(f"Nota média {media}. Aluno reprovado.")
elif media >=7 and media < 10:
    print(f"Nota média {media}. Aluno aprovado")
elif media == 10:
    print(f"Nota média {media}. Aluno aprovado com distinção.")
else:
    print("Nota informada inválida.")
