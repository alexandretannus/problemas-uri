"""  
    URI Online Judge 
	Problema 1467 - Zerinho ou UM
    https://www.urionlinejudge.com.br/repository/UOJ_1467.html 
 """

while True:
    try:
        a, b, c = input().split()
        
        if (a != b and b == c):
            print("A")
        elif (a != b and a == c):
            print("B")
        elif (b != c and a == b):
            print("C")
        else:
            print("*")

        
    except EOFError:
        break