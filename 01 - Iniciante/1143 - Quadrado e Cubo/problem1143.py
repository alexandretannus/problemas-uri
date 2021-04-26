""" 
	URI Online Judge 
	Problema 1143 - Quadrado e Cubo
    https://www.urionlinejudge.com.br/repository/UOJ_1143.html 
"""

num = int(input())

for n in range(num):
    k = n+1
    quad = k * k
    cubo = k * k * k
    print('{0} {1} {2}'.format(k, quad, cubo))