""" 
	URI Online Judge 
	Problema 1072 - Intervalos 2
    https://www.urionlinejudge.com.br/repository/UOJ_1065.html 
"""
casos = int(input())
in1 = 0
out1 = 0
for caso in range(casos):
    num = int(input())
    if num >= 10 and num <= 20:
        in1 += 1
    else:
        out1 += 1

print '%i in' % in1
print '%i out' % out1