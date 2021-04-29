""" 
	URI Online Judge 
	Problema 1094 - Experiências
    https://www.urionlinejudge.com.br/repository/UOJ_1094.html 
"""

casos = int(input())

quantidade = {
    "rato": 0,
    "coelho": 0,
    "sapo": 0
}

percentual = {
    "rato": 0,
    "coelho": 0,
    "sapo": 0
}

total = 0

for caso in range(casos):
    qtd, tipo = input().split()

    if (tipo == 'R'):
        quantidade["rato"] += int(qtd)
    
    if (tipo == 'C'):
        quantidade["coelho"] += int(qtd)
    
    if (tipo == 'S'):
        quantidade["sapo"] += int(qtd)
    
    total += int(qtd)

percentual["rato"] = 100 * quantidade["rato"] / total
percentual["coelho"] = 100 * quantidade["coelho"] / total
percentual["sapo"] = 100 * quantidade["sapo"] / total

print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % quantidade["coelho"])
print("Total de ratos: %d" % quantidade["rato"])
print("Total de sapos: %d" % quantidade["sapo"])
print("Percentual de coelhos: %.2f %%" % percentual["coelho"])
print("Percentual de ratos: %.2f %%" % percentual["rato"])
print("Percentual de sapos: %.2f %%" % percentual["sapo"])