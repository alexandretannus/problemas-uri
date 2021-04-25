""" 
	URI Online Judge 
	Problema 1015 - Distância Entre Dois Pontos
    https://www.urionlinejudge.com.br/repository/UOJ_1015.html
 """

import math

x1, y1 = input().split()
x2, y2 = input().split()

fx1 = float(x1)
fy1 = float(y1)
fx2 = float(x2)
fy2 = float(y2)

x12 = math.pow((fx2 - fx1), 2)
y12 = math.pow((fy2 - fy1), 2)
distancia = math.sqrt(x12 + y12)

print("%.4f" % distancia)