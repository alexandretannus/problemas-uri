#include <iostream>
#include <cmath>
using namespace std;

int fatorial(int n);

int main() {

	int acm, dec, soma, resto, index;
    int fatorial[5] = {1, 2, 6, 24, 120};

	while (1) {	
		scanf("%d", &acm);
		
		if (acm == 0) {
			break;
		}
		
		dec = 0;
		index = 0;
		while (acm != 0) {
			resto = acm%10;
			acm = acm/10;
			dec += resto * fatorial[index];
            index++;
		}
		
		printf("%d\n", dec);
		
	}
    return 0;
}
