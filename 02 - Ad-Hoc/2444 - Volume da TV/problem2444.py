"""  
    URI Online Judge 
	Problema 2444 - Volume da TV
    https://www.urionlinejudge.com.br/repository/UOJ_2444.html 
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