""" 
	URI Online Judge 
	Problema 1013 - O maior
    https://www.urionlinejudge.com.br/repository/UOJ_1013.html
 """

import math

def maior(a, b):
    maiorAB = (a + b + math.fabs(a-b))/2.0
    return maiorAB

a, b, c = input().split()

ia = int(a)
ib = int(b)
ic = int(c)

maiorAB = maior(ia, ib)
maiorABC = maior(maiorAB, ic)

print("%d eh o maior" % maiorABC)