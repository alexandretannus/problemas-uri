#include <iostream>
 
using namespace std;

int calcularCarry(unsigned long x, unsigned long y);
void imprimirResposta(int carry);

int main() {
	unsigned long x, y;
	int carry;
	
	while (1) {
		
		cin >> x >> y;		

		if (x == 0  && y == 0) {
			break;
		}
		
		carry = calcularCarry(x, y);
		
		imprimirResposta(carry);	
	} 


    return 0;
}

int calcularCarry(unsigned long x, unsigned long y) {
	unsigned long rx, ry;
	int carry = 0, sumCarry = 0;

	while (x || y) {
		rx = x%10;
		ry = y%10;
		
		if ((rx + ry + carry) > 9) {
			sumCarry++;
			carry = 1;
		} else {
			carry = 0;
		}	
		
		x /= 10;
		y /= 10;
		
	} 
	
	return sumCarry;
}

void imprimirResposta(int carry) {		
	if (carry == 0) {
		cout << "No carry operations." << endl;
	} else if (carry == 1) {
		cout << "1 carry operation." << endl;		
	} else {
		cout << carry << " carry operations." << endl;		
	}
}
