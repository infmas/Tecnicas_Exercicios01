""""
Aluno: Marco Antonio Schwertner
Disciplina: Técnicas de Programação
Professor: Luiz Gonzaga da Silveira Junior
Semestre: 2018/1
Trabalho: Lista de exercícios 01, exercício 07
"""

def ValidaInteiro(numero):
    try:
        valido = True
        int(numero)
    except ValueError:
        valido = False   #indica número inválido
    return valido

numero = input("Informe um número inteiro: ")
if not ValidaInteiro(numero):
    print("Número inteiro informado é inválido.")
    quit()
numero = int(numero)

#par ou ímpar
if numero % 2 == 0:
    print (f"O número inteiro {numero} é par.")
else:
    print (f"O número inteiro {numero} é ímpar.")

#número perfeito
divisores = []
for index in range(1,numero):
    if numero % index == 0:
        divisores.append(index)
soma=0
for item in divisores:
    soma += item
if soma == numero:
    print(f"O número inteiro {numero} é um número perfeito.")
else:
    print(f"O número inteiro {numero} não é um número perfeito.")

#número primmo
isPrimo = True
for index in range (2,numero-1):
    if numero % index == 0:
        isPrimo=False
        break
if isPrimo:
    print(f"O número inteiro {numero} é um número primo.")
else:
    print(f"O número inteiro {numero} não é um número primo.")