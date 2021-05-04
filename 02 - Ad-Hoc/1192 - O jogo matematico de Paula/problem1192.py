"""  
    URI Online Judge 
	Problema 1192 - O jogo Matematico de Paula
    https://www.urionlinejudge.com.br/repository/UOJ_1192.html 
 """

casos = int(input())

for caso in range(casos):
    teste = input()

    letra = teste[1]
    num1 = int(teste[0])
    num2 = int(teste[2])
    if num1 == num2:
        res = num1 * num2
    else:
        if (letra >= "A" and letra <= "Z"):
            res = num2 - num1
        else:
            res = num1 + num2

    print(res)
