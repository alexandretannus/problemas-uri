""" 
	URI Online Judge 
	Problema 1071 - Soma de Impares Consecutivos
    https://www.urionlinejudge.com.br/repository/UOJ_1071.html 
"""

num1 = int(input())
num2 = int(input())

maior = num1 if num1 > num2 else num2
menor = num1 if num1 < num2 else num2
soma = 0

for i in range(menor, maior+1):
    if (i % 13):
        soma += i

print(soma)