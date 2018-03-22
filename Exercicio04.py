""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 04
"""

def ValidaPreco(preco):
    try:
        precoValidado = float(preco)
        if precoValidado < 0:
            precoValidado = -1   #indica valor negativo
    except ValueError:
        precoValidado = -2   #indica número inválido

    return precoValidado


precos = []
for index in range(3):
    precos.append(ValidaPreco(input(f"Informe o preço {index+1}: ")))
    if precos[index] < 0:
        if precos[index] == -1:
            print("Preço não pode ser negativo.")
        elif precos[index] == -2:
            print("Preço informado é inválido.")
        quit()

menorPreco = precos[0]
for preco in precos:
    if menorPreco > preco:
        menorPreco = preco

print(f"O menor preço é: {menorPreco}")