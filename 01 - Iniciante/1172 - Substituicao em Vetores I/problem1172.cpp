/*
	URI Online Judge
	Problema 1172 - Substituição em Vetor I
	
	Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos 
	e negativos do vetor X por 1. Em seguida mostre o vetor X.
	
	Entrada
	A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.
	
	Saída
	Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o 
	valor armazenado naquela posição.
	
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
