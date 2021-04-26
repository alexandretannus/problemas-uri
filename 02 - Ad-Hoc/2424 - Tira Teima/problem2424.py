""" 
	URI Online Judge 
	Problema 2424 - Tira Teima
    https://www.urionlinejudge.com.br/repository/UOJ_2424.html
 """

x, y = map(int, raw_input().split())  

if (x >= 0 and x <= 432 and y >= 0 and y <= 468):
    print("dentro")
else:
    print("fora")