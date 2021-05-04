""" 
	URI Online Judge 
	Problema 1151 - Fibonacci Facil
    https://www.urionlinejudge.com.br/repository/UOJ_1151.html 
"""

def calcularFibonacci(n):
    anterior = 0
    atual = 1
    text = "0 1 " 
    for i in range(2, n):
        tmp = atual
        atual += anterior
        anterior = tmp
        text += str(atual)
        if i < n-1:
            text += " "
    print(text)

n = int(input())
calcularFibonacci(n)