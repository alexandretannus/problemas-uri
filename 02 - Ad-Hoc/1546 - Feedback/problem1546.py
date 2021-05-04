"""  
    URI Online Judge 
	Problema 1546 - Feedback
    https://www.urionlinejudge.com.br/repository/UOJ_1546.html 
 """

casos = int(input())

staff = ["", "Rolien", "Naej", "Elehcim", "Odranoel"]

for caso in range(casos):
    feeds = int(input())
    for feed in range(feeds):
        resp = int(input())
        print(staff[resp])