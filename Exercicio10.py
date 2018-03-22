""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 10
"""

lista = input("Informe a lista separando os itens com \",\": ").split(",")
metade = len(lista) // 2
isPalindromo = True
posicao = -1
for item in lista[:metade]:
    if item != lista[posicao]:
        isPalindromo = False
        break
    else:
        posicao -= 1

if isPalindromo:
    print(f"A lista é um palíndromo.\nLista: {lista}")
else:
    print(f"A lista não é um palíndromo.\nLista: {lista}")    