	"""   
		URI Online Judge 
		Problema 1240 - Encaixa ou Não I
		https://www.urionlinejudge.com.br/repository/UOJ_1240.html
	"""
	casos = int(input())

	for i in range(casos):
		pot = 1
		"""
		Python 2.7 
		a, b = map(int, raw_input().split()) 
		"""

		a, b = input().split()	
		n = int(b)
		
		while (int(n)!=int(0)):
			n /= 10
			pot *= 10
		
		if int(a)%pot == int(b):
			print("encaixa")
		else:
			print("nao encaixa")
