""" 
	URI Online Judge 
	Problema 1533 - Detetive Watson
    https://www.urionlinejudge.com.br/repository/UOJ_1533.html
 """


while (1):
    casos = int(input())

    maior = 0
    maior2 = 0
    if (casos == 0):
        break
        
    suspects = input().split()

    for i in range(casos):
        if int(suspects[i]) > int(maior2):
            maior2 = suspects[i]
        if int(suspects[i]) > int(maior):
            maior2 = maior
            maior = suspects[i]
    print(maior)
    print(suspects.index(maior2)+1)