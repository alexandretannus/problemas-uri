"""  
    URI Online Judge 
	Problema 1091 - Divisao da Nlogonia
    https://www.urionlinejudge.com.br/repository/UOJ_1091.html 
 """

def definirRegiao(coordX, coordY, divisaX, divisaY):
    if divisaX == coordX or divisaY == coordY:
        return "divisa"
    else:
        if coordX > divisaX and coordY > divisaY:
            return "NE"            
        elif coordX > divisaX and coordY < divisaY:
            return "SE"
        elif coordX < divisaX and coordY > divisaY:
            return "NO"
        else:
            return "SO"
    

while True:
    casos = int(input())

    if casos == 0:
        break
    
    dx, dy = map(int, input().split())
    for caso in range(casos):
        x, y = map(int, input().split())
        regiao = definirRegiao(x, y, dx, dy)
        print(regiao)