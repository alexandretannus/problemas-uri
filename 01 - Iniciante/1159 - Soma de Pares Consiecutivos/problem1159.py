"""  
    URI Online Judge 
	Problema 1159 - Soma de Pares Consecutivos
    https://www.urionlinejudge.com.br/repository/UOJ_1159.html 
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
while True:
    num = int(input())
    soma = 0 
    if num == 0:
        break

    for i in range(5):
        if num % 2 == 0:
            soma += num + 2*i
        else:
            soma += (num+1) + 2*i
    
    print(soma)