/*  
	URI Online Judge 
	Problema 1169 - Trigo no Tabuleiro
    https://www.urionlinejudge.com.br/repository/UOJ_1169.html
*/

#include <iostream>
#include <cmath>
using namespace std;
 
int main() {

	int n, x;
	unsigned long long int total;
	scanf("%d", &n);
	
	for (int i=0; i<n; i++) {
		scanf("%d", &x);
		
		total = pow(2, x) / 12000;
		
		printf("%lld kg\n", total);
	}
	

    return 0;
}