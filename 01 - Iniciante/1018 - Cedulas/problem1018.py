""" 
	URI Online Judge 
	Problema 1018 - Cédulas
    https://www.urionlinejudge.com.br/repository/UOJ_1018.html
 """
valor = input()
notas = [100, 50, 20, 10, 5, 2, 1]
qtd = [0]*7

qtd[0] = int(valor) / notas[0]
r = int(valor) % 100

for i in range(1,6):
    qtd[i] = r / notas[i]
    r %= notas[i]

qtd[6] = r

print(valor)
for i in range(0,7):
    print(f'{int(qtd[i])} nota(s) de R$ {notas[i]},00')    
