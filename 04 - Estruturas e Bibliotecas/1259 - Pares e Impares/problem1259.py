"""  
    URI Online Judge 
	Problema 1259 - Pares e Impares
    https://www.urionlinejudge.com.br/repository/UOJ_1259.html 
 """

def alterarVolume(volume, alteracao): 
    volume = volumeAtual + int(alteracao)
    
    volume = 100 if volume > 100 else volume    
    volume = 0 if volume < 0 else volume
    
    return volume

volumeInicial, alteracoes = input().split()

mudancas = input().split()
volumeAtual = int(volumeInicial)
for mudanca in mudancas:    
    volumeAtual = alterarVolume(volumeAtual, mudanca)

print(volumeAtual)

casos = int(input())
pares = []
impares = []
for caso in range(casos):
    item = int(input())
    if item % 2:
        impares.append(item)
    else:
        pares.append(item)

pares.sort()
impares.sort(reverse=True)
for num in pares:
    print(num)
for num in impares:
    print(num)