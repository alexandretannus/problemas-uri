""" 
	URI Online Judge 
	Problema 1065 - Pares entre Cinco Números
    https://www.urionlinejudge.com.br/repository/UOJ_1065.html 
"""
par = 0
for i in range(5):
    num = int(input())
    if num % 2 == 0:
        par += 1

print '%i valores pares' % par
