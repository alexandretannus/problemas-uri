""" 
	URI Online Judge 
	Problema 1101 - Sequencia de Numeros e Soma
    https://www.urionlinejudge.com.br/repository/UOJ_1101.html 
"""

while(1):
    num1, num2 = map(int, input().split())
    
    if (num1 <= 0 or num2 <= 0):
        break

    maior = num1 if num1 > num2 else num2
    menor = num1 if num1 < num2 else num2
    soma = 0
    texto = ""


    for num in range(menor, maior+1):
        soma += num
        texto += str(num) + " "

    texto += "Sum=%i" % soma
    print(texto)