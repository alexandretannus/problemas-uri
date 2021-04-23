/*
	URI Online Judge
	Problema 1175 - Troca em Vetor I
	
	Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, 
	o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.
	
	Entrada
	A entrada contém 20 valores inteiros, positivos ou negativos.
	
	Saída
	Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor 
	armazenado naquela posição.
		
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
