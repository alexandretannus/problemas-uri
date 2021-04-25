""" 
	URI Online Judge 
	Problema 1010 - Cálculo Simples
    https://www.urionlinejudge.com.br/repository/UOJ_1010.html
 """

codigo1, num1, valor1 = input().split()
codigo2, num2, valor2 = input().split()

total = int(num1) * float(valor1) + int(num2) * float(valor2)

print("VALOR A PAGAR: R$ %.2f" % total)