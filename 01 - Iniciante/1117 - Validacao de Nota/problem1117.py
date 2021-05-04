""" 
	URI Online Judge 
	Problema 1117 - Validacao de Nota
    https://www.urionlinejudge.com.br/repository/UOJ_1114.html 
"""

validas = 0
soma = 0
while validas < 2:
    nota = float(input())

    if nota >= 0 and nota <= 10:
        validas += 1
        soma += nota
    else:
        print("nota invalida")
    
media = soma/2
print("media = %.2f" % media)