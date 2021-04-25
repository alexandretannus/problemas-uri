""" 
	URI Online Judge 
	Problema 1011 - Esfera
    https://www.urionlinejudge.com.br/repository/UOJ_1011.html
 """
import math

raio = input()
pi = float(3.14159)

volume = (4/3.0) * pi * math.pow(float(raio), 3)

print("VOLUME = %.3f" % volume)