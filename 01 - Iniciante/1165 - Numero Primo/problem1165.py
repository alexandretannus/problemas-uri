""" 
	URI Online Judge 
	Problema 1165 - Numero Primo
    https://www.urionlinejudge.com.br/repository/UOJ_1165.html 
"""
import math

def verificarPrimo(numero):
    raiz = int(math.sqrt(numero))

    if numero < 2:
        return 0

    for i in range(2, raiz+1):
        if (num % i == 0):
            return 0

    return 1

casos = int(input())

for caso in range(casos):
    num = int(input())

    if (verificarPrimo(num)):
        print("%i eh primo" % num)
    else:
        print("%i nao eh primo" % num)