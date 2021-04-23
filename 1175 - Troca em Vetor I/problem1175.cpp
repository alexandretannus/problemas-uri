/*
	URI Online Judge
	Problema 1175 - Troca em Vetor I
	
	Fa�a um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o �ltimo, 
	o segundo elemento com o pen�ltimo, etc., at� trocar o 10� com o 11�. Mostre o vetor modificado.
	
	Entrada
	A entrada cont�m 20 valores inteiros, positivos ou negativos.
	
	Sa�da
	Para cada posi��o do vetor N, escreva "N[i] = Y", onde i � a posi��o do vetor e Y � o valor 
	armazenado naquela posi��o.
		
*/

#include <iostream>
 
using namespace std;

int main() {
    
    int tam = 20, n[tam], temp;
    
    for (int j=0; j<tam; j++){
    	scanf("%d", &n[j]);
	}
    	
    
    for (int i=0; i<tam/2; i++) {
    	temp = n[i];
    	n[i] = n[(tam-1)-i];
		n[(tam-1)-i] = temp;       
    }   
	 
    for (int k=0; k<tam; k++) {    	     
        printf("N[%d] = %d\n", k, n[k]);
    }
 
    return 0;
}
