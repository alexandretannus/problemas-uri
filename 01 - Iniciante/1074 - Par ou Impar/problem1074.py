""" 
	URI Online Judge 
	Problema 1074 - Par ou Impar
    https://www.urionlinejudge.com.br/repository/UOJ_1074.html 
"""

casos = int(input())

resp = ""
for caso in range(casos): 
    num = int(input())

    resp = "ODD" if num % 2 == 1 else "EVEN"
    resp += " NEGATIVE" if num < 0 else " POSITIVE"
    if num == 0:
        resp = "NULL"

    print(resp)