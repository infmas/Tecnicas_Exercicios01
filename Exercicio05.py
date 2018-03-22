""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 05
"""

numeros = []
for index in range(2000, 7000):
    if index % 3 == 0 and index % 5 != 0:
        numeros.append(index)

print(f"Lista de números divisíveis por 3 e não múltiplos de 5:\nForam encontrados {len(numeros)} números.\n{numeros}")