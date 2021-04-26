/*  
	URI Online Judge 
	Problema 1240 - Encaixa ou Não I
    https://www.urionlinejudge.com.br/repository/UOJ_1240.html
*/

#include <iostream>
#include <cmath>
using namespace std;


int main() {
	
	int a, b, tam, n, casos, pot;
	scanf("%d", &casos);
	
	for (int i=0; i<casos; i++) {
		scanf("%d %d", &a, &b);
		tam = 0;
		n = b;
		while (n!=0){
			n /= 10;
			tam++;
		}
		pot = pow(10,tam);
		
		if (a%pot == b) {
			printf("encaixa\n");
		} else {
			printf("nao encaixa\n");
		}
	}
    return 0;
}

