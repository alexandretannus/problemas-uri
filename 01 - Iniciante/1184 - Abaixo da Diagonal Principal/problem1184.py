""" 
	URI Online Judge 
	Problema 1184 - Abaixo da Diagonal Principal
    https://www.urionlinejudge.com.br/repository/UOJ_1184.html 
"""

def preencherMatriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(float(input()))
        matriz.append(linha)

    return matriz

def calcularDiagonalPrincipal(matriz, ordem, op):
    soma = 0
    elementos = 0
    for linha in range(ordem):
        for coluna in range(linha+1, ordem):
            soma += matriz[coluna][linha] 
            elementos += 1
            
    return soma if op == 'S' else soma/elementos

operacao = input()
ordem = 12

matriz = preencherMatriz(ordem)
result = calcularDiagonalPrincipal(matriz, ordem, operacao)

print("%.1f" % result)

