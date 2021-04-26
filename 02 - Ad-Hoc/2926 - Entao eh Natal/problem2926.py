""" 
	URI Online Judge 
	Problema 2926 - Entao eh Natal
    https://www.urionlinejudge.com.br/repository/UOJ_2926.html
 """

n = int(input())

s = "Entao eh Natal!"
s1 = "a"*n

s2 = s.replace("a", s1, 3)

print(s2)