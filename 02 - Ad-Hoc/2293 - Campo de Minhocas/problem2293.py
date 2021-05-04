""" 
	URI Online Judge 
	Problema 2293 - Campo de Minhocas
    https://www.urionlinejudge.com.br/repository/UOJ_2293.html 
"""

def obterMaximoLinha(matriz, numLinha, numColuna):
    maior = 0
    for i in range(numLinha):
        soma = 0
        for j in range(numColuna):
            soma += int(matriz[i][j])
        if (soma > maior):
            maior = soma
    
    return maior

def obterMaximoColuna(matriz, numLinha, numColuna):
    maior = 0
    for i in range(numColuna):
        soma = 0
        for j in range(numLinha):
            soma += int(matriz[j][i])
        
        if (soma > maior):
            maior = soma
    
    return maior

def preencherMatriz(numLinhas, numColunas):
    matriz = []
    for i in range(numLinhas):
        newLine = input().split()
        matriz.append(newLine)

    return matriz

linhas, colunas = map(int, input().split())


matriz = preencherMatriz(linhas, colunas)
maxLinha = obterMaximoLinha(matriz, linhas, colunas)
maxColuna = obterMaximoColuna(matriz, linhas, colunas)

maximo = maxLinha if maxLinha > maxColuna else maxColuna

print(maximo)
