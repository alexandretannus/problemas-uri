
def calcularCarry(x,  y):
	sumCarry = 0
	carry = 0

	while (x or y): 
		rx = x % 10
		ry = y % 10
		
		if ((rx + ry + carry) > 9): 
			sumCarry += 1
			carry = 1
		else: 
			carry = 0
				
		x /= 10
		y /= 10
	
	
	return sumCarry


def imprimirResposta(carry): 		
	if (carry == 0): 
		print("No carry operations.")
	elif (carry == 1):
		print("1 carry operation.")		
	else:
		print("%i carry operations." % carry)			


while True:
    
    x, y = input().split()		

    if (int(x) == 0  and int(y) == 0): 
        break;
    
    
    carry = calcularCarry(int(x), int(y))
    
    imprimirResposta(carry)		

