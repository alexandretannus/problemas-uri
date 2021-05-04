"""  
    URI Online Judge 
	Problema 1943 - Top N
    https://www.urionlinejudge.com.br/repository/UOJ_1943.html 
 """

k = int(input())

if k == 1:
    s = "Top 1"
elif k > 1 and k <= 3:
    s = "Top 3"
elif k > 3 and k <= 5:
    s = "Top 5"
elif k > 5 and k <= 10:
    s = "Top 10"
elif k > 10 and k <= 25:
    s = "Top 25"
elif k > 25 and k <= 50:
    s = "Top 50"
elif k > 50 and k <= 100:
    s = "Top 100"

print(s)