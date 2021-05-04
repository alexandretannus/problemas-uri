""" 
	URI Online Judge 
	Problema 1164 - Numero Perfeito
    https://www.urionlinejudge.com.br/repository/UOJ_1164.html 
"""
import math

def verificarPerfeito(numero):
    raiz = int(math.sqrt(numero))
    soma = 1

    if numero < 2:
        return 0

    for i in range(2, raiz+1):
        if (num % i == 0):
            soma += i
            soma += int(num/i)

    return 1 if soma == numero else 0

casos = int(input())

for caso in range(casos):
    num = int(input())

    if (verificarPerfeito(num)):
        print("%i eh perfeito" % num)
    else:
        print("%i nao eh perfeito" % num)