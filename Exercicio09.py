""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 09
"""

def ValidaInteiro(numero):
    try:
        valido = True
        int(numero)
    except ValueError:
        valido = False   #indica número inválido
    return valido

def GeraLista(listaNome):
    tamanho = input(f"Informe o tamanho da lista {listaNome}: ")
    if not ValidaInteiro(tamanho):
        print("Tamanho informado é inválido.")
        quit()
    else:
        tamanho = int(tamanho)
    rangeIni = input(f"Informe o início da faixa de números para a a lista {listaNome}: ")
    if not ValidaInteiro(rangeIni):
        print("Valor informado é inválido.")
        quit()
    else:
        rangeIni = int(rangeIni)
    rangeFim = input(f"Informe o início da faixa de números para a a lista {listaNome}: ")
    if not ValidaInteiro(rangeFim):
        print("Valor informado é inválido.")
        quit()
    else:
        rangeFim = int(rangeFim)
    
    lista = []
    rangeAtual = rangeIni
    for _ in range (tamanho):
        lista.append(rangeAtual)
        rangeAtual += 1
        if rangeAtual > rangeFim:
            rangeAtual = rangeIni
    return lista


listaA = GeraLista("A")
listaB = GeraLista("B")

listaComum = []
for itemA in listaA:
    if itemA in listaB and itemA not in listaComum:
        listaComum.append(itemA)

print (f"Lista A: {listaA}")
print (f"Lista B: {listaB}")
print (f"Lista com os itens em comum: {listaComum}")