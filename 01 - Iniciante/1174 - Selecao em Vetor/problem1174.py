""" 
	URI Online Judge 
	Problema 1174 - Selecao em Vetor I
    https://www.urionlinejudge.com.br/repository/UOJ_1174.html 
"""

def lerVetor(vetor):
    for i in range(10):
        vetor.append(float(input()))

def imprimirVetor(vetor):
    for i in range(10):
        if vetor[i] <= 10:
            print("A[%i] = %.1f" % (i, vetor[i]))

vetor = []
lerVetor(vetor)
imprimirVetor(vetor)