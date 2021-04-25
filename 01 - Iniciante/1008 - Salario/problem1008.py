""" 
	URI Online Judge 
	Problema 1008 - Salário
    https://www.urionlinejudge.com.br/repository/UOJ_1008.html
 """

numero = input()
valorHora = input()
horasTrabalhadas = input()

salario = int(valorHora) * horasTrabalhadas

print("NUMBER =", numero)
print("SALARY = U$ %.2f" % salario)