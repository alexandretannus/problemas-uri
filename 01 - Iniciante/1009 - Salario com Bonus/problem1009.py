""" 
	URI Online Judge 
	Problema 1009 - Salário com Bônus
    https://www.urionlinejudge.com.br/repository/UOJ_1008.html
 """

nome = input()
salario = input()
vendas = input()

total = float(salario) + 0.15 * float(vendas)

print("TOTAL = R$ %.2f" % total)