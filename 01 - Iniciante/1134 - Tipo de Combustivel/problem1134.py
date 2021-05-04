""" 
	URI Online Judge 
	Problema 1134 - Tipo de Combustivel
    https://www.urionlinejudge.com.br/repository/UOJ_1114.html 
"""

quantidade = { "alcool": 0, "gasolina": 0, "diesel": 0 }

while (1):
    escolha = int(input())

    if (escolha == 4):
        break

    if (escolha == 1): 
        quantidade["alcool"] += 1
    elif (escolha == 2):
        quantidade["gasolina"] += 1
    elif (escolha == 3):
        quantidade["diesel"] += 1

print("MUITO OBRIGADO")
print("Alcool: %i" % quantidade["alcool"])
print("Gasolina: %i" % quantidade["gasolina"])
print("Diesel: %i" % quantidade["diesel"])