#include <iostream>
 
using namespace std;
 
int main() {

	int x, y, carry, rx, ry, cont;
	
	while (1) {
		int c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}; 
		scanf("%d %d", &x, &y);
		if (!x && !y) {
			break;
		}
		carry = 0;
		cont = 0;
		do {
			rx = x%10;
			ry = y%10;
			x = x/10;
			y = y/10;
			
			if (rx + ry + c[cont] > 9) {
				c[cont+1] = 1;
				carry++;
			}
			
			cont++;
			
		} while (x || y);		
		
		
		
		if (!carry) {
			printf ("No carry operations.\n");
		} else if (carry == 1) {
			printf ("%d carry operation.\n", carry);		
		} else {
			printf ("%d carry operations.\n", carry);		
		}		
	} 


    return 0;
}
