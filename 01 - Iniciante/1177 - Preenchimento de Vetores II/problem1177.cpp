/*
	URI Online Judge
	Problema 1177 - Preenchimento de Vetor II
	
	Fa�a um programa que leia um valor T e preencha um vetor N[1000] com a sequ�ncia de valores 
	de 0 at� T-1 repetidas vezes, conforme exemplo abaixo. Imprima o vetor N.

	Entrada
	A entrada cont�m um valor inteiro T (2 <= T <= 50).
	
	Sa�da
	Para cada posi��o do vetor, escreva "N[i] = x", onde i � a posi��o do vetor e x � o valor 
	armazenado naquela posi��o.
	
*/

#include <iostream>
 
using namespace std;

int main() {
    
    int valor, n[1000];
    
    scanf("%d", &valor);
    
    for (int i=0; i<1000; i++) {
        n[i] = i%valor;
        printf("N[%d] = %d\n", i, n[i]);
    }
 
    return 0;
}
