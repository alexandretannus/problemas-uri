""" 
	URI Online Judge 
	Problema 1397 - Jogo do maior
    https://www.urionlinejudge.com.br/repository/UOJ_1397.html
 """
while(1):
    jogos = int(input())

    if (jogos == 0):
        break

    p1 = p2 = 0

    for i in range(jogos):
        n1, n2 = map(int, input().split())

        if n1 > n2:
            p1 += 1
        elif n2 > n1:
            p2 += 1
        
    print(p1, p2)