""" 
	URI Online Judge 
	Problema 1080 - Maior e posicao
    https://www.urionlinejudge.com.br/repository/UOJ_1080.html 
"""

maior = 0
pos = 0
for i in range(10):
    num = int(input())
    if num > maior:
        maior = num
        pos = i+1

print(maior)
print(pos)