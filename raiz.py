#Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, 
#identificando quais resultaram em um número inteiro. A lista é a seguinte:

import math

numeros = [2, 8, 15, 23, 91, 112, 256]
raiz_calculada = []

for numero in numeros:
    raiz = math.sqrt(numero)
    raiz_calculada.append(raiz)
    print(f"A raiz quadrada de {numero} é {raiz:.2f}")

for i in range(len(numeros)):
    raiz_atual = raiz_calculada[i]
    if raiz_atual % 1 == 0:
        print(f"A raiz quadrada de {numeros[i]} é um número inteiro: {int(raiz_atual)}")