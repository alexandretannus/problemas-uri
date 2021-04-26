""" 
	URI Online Judge 
	Problema 2369 - Conta de Agua
    https://www.urionlinejudge.com.br/repository/UOJ_2369.html
 """
consumo = int(input())

if consumo <= 10:
    valor = 7
elif consumo > 10 and consumo <= 30:
    valor = 7 + (consumo-10)
elif consumo > 30 and consumo <= 100:
    valor = 7 + 20 + (consumo - 30)*2
else:
    valor = 7 + 20 + 140 + (consumo - 100)*5

print(valor)