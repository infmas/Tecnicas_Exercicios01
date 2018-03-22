""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 02
"""

vogal = ["A","E","I","O","U"]
consoante = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Z"]
letra = str(input("Informe uma letra:"))

if (len(letra) != 1):
    print ("Informe apenas uma letra.")
    quit()
else:
    if letra.upper() in vogal:
        print(f"A letra informada {letra} é uma vogal.")
    elif letra.upper() in consoante:
        print(f"A letra informada {letra} é uma consoante.")
    else:
        print(f"A letra informada {letra} não foi reconhecida como vogal ou consoante.")