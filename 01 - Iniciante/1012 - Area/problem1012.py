""" 
	URI Online Judge 
	Problema 1012 - Area
    https://www.urionlinejudge.com.br/repository/UOJ_1012.html
 """
import math

a, b, c = input().split()
pi = float(3.14159)

fa = float(a)
fb = float(b)
fc = float(c)

triangulo = fa * fc/2.0
circulo = pi * math.pow(fc, 2)
trapezio = (fa + fb)*fc/2.0
quadrado = math.pow(fb, 2)
retangulo = fa * fb

print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)