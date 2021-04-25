""" 
	URI Online Judge 
	Problema 1017 - Gasto de Combustível
    https://www.urionlinejudge.com.br/repository/UOJ_1017.html
 """

t = input()
v = input()

dist = int(t) * int(v) / 12.0

print("%.3f" % dist)