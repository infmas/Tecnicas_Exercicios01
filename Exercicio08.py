""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 08
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listaComum = []

for itemA in a:
    if itemA in b and itemA not in listaComum:
        listaComum.append(itemA)

print (f"Lista a: {a}")
print (f"Lista b: {b}")
print (f"Lista com os itens em comum: {listaComum}")