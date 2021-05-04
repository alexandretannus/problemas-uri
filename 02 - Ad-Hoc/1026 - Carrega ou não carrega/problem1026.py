"""  
    URI Online Judge 
	Problema 1026 - Carrega ou Não Carrega?
    https://www.urionlinejudge.com.br/repository/UOJ_1026.html 
 """

while True:
    try:
        x, y = input().split()
        result = int(x) ^ int(y)
        print(result)
    except EOFError:
        break