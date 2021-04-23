/*
	URI Online Judge
	Problema 1172 - Substitui��o em Vetor I
	
	Fa�a um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos 
	e negativos do vetor X por 1. Em seguida mostre o vetor X.
	
	Entrada
	A entrada cont�m 10 valores inteiros, podendo ser positivos ou negativos.
	
	Sa�da
	Para cada posi��o do vetor, escreva "X[i] = x", onde i � a posi��o do vetor e x � o 
	valor armazenado naquela posi��o.
	
*/

#include <iostream>
 
using namespace std;

int main() {
    
    int n[10];
    
    for (int j=0; j<10; j++){
    	scanf("%d", &n[j]);
	}
    	
    
    for (int i=0; i<10; i++) {
    	if (n[i] <= 0){
    		n[i] = 1;	
		}        
        printf("X[%d] = %d\n", i, n[i]);
    }
 
    return 0;
}
