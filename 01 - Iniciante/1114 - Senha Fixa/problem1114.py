""" 
	URI Online Judge 
	Problema 1114 - Senha Fixa
    https://www.urionlinejudge.com.br/repository/UOJ_1114.html 
"""

senhaCerta = 2002

while(1):
    senha = int(input())

    if (senha == senhaCerta):
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
    