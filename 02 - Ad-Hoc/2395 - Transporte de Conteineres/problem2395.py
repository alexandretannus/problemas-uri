"""  
    URI Online Judge 
	Problema 2395 - Transporte de Conteineres
    https://www.urionlinejudge.com.br/repository/UOJ_2395.html 
 """

cx, cy, cz = map(int, input().split())
nx, ny, nz = map(int, input().split())

t = int(nx/cx) * int(ny/cy) * int(nz/cz)

print(t)
