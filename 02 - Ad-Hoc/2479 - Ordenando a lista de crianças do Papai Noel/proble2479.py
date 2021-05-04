"""  
    URI Online Judge 
	Problema 2479 - Ordenando a Lista de Crianças do Papai Noel
    https://www.urionlinejudge.com.br/repository/UOJ_2479.html 
 """

n = int(input())

c = 0
nc = 0
lista = []

for i in range(n):
    s, nome = input().split()
    lista.append(nome)
    if s == '+':
        c += 1
    else:
        nc += 1
    
lista.sort()

for p in lista:
    print(p)

print('Se comportaram: %i | Nao se comportaram: %i' % (c, nc))