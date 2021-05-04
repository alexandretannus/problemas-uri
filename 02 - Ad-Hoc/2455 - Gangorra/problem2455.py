"""  
    URI Online Judge 
	Problema 2455 - Gangorra
    https://www.urionlinejudge.com.br/repository/UOJ_2455.html 
 """

p1, c1, p2, c2 = map(int, input().split())

e1 = p1 * c1
e2 = p2 * c2

if (e1 == e2):
    print(0)
elif (e1 > e2):
    print(-1)
else:
    print(1)