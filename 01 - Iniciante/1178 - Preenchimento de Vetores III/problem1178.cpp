/*
	URI Online Judge
	Problema 1178 - Preenchimento de Vetor III
	
	Leia um valor X. Coloque este valor na primeira posi��o de um vetor N[100]. 
	Em cada posi��o subsequente de N (1 at� 99), coloque a metade do valor armazenado 
	na posi��o anterior, conforme o exemplo abaixo. Imprima o vetor N.
	
	Entrada
	A entrada contem um valor de dupla precis�o com 4 casas decimais.
	
	Sa�da
	Para cada posi��o do vetor N, escreva "N[i] = Y", onde i � a posi��o do vetor e Y 
	� o valor armazenado naquela posi��o. Cada valor do vetor deve ser apresentado com 4 casas decimais.
	
*/

#include <iostream>
 
using namespace std;

int main() {
    
    double valor, n[100];
    
    scanf("%lf", &valor);
    n[0] = valor;
    printf("N[0] = %.4lf\n", n[0]);
    
    for (int i=1; i<100; i++) {
        n[i] = n[i-1]/2;
        printf("N[%d] = %.4lf\n", i, n[i]);
    }
 
    return 0;
}
