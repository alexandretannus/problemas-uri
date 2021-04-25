""" 
	URI Online Judge 
	Problema 1014 - Consumo
    https://www.urionlinejudge.com.br/repository/UOJ_1014.html
 """

distancia = input()
combustivel = input()

consumo = int(distancia) / float(combustivel)

print("%.3f km/l" % consumo)