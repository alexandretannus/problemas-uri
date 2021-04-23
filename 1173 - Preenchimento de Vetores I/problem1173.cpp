/*
	URI Online Judge
	Problema 1173 - Preenchimento de Vetor I
	
*/

#include <iostream>
 
using namespace std;

int main() {
    
    int n[10];
    
    scanf("%d", &n[0]);
    printf("N[0] = %d\n", n[0]);
    
    for (int i=1; i<10; i++) {
        n[i] = n[i-1]*2;
        printf("N[%d] = %d\n", i, n[i]);
    }
 
    return 0;
}
