""" 
	URI Online Judge 
	Problema 1181 - Linha na Matriz
    https://www.urionlinejudge.com.br/repository/UOJ_1181.html 
"""

def preencherMatriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(float(input()))
        matriz.append(linha)

    return matriz

def calcularEmLinha(matriz, linha, ordem, op):
    soma = 0
    for coluna in range(ordem):
        soma += matriz[linha][coluna]
    
    return soma if op == 'S' else soma/12

linha = int(input())
operacao = input()
ordem = 12

matriz = preencherMatriz(ordem)
result = calcularEmLinha(matriz, linha, ordem, operacao)

print("%.1f" % result)

