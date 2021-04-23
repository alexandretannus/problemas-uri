/*
	URI Online Judge
	Problema 1178 - Preenchimento de Vetor III
	
	Leia um valor X. Coloque este valor na primeira posição de um vetor N[100]. 
	Em cada posição subsequente de N (1 até 99), coloque a metade do valor armazenado 
	na posição anterior, conforme o exemplo abaixo. Imprima o vetor N.
	
	Entrada
	A entrada contem um valor de dupla precisão com 4 casas decimais.
	
	Saída
	Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y 
	é o valor armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.
	
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
