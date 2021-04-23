/*
	URI Online Judge
	Problema 1179 - Preenchimento de Vetor IV
	https://www.urionlinejudge.com.br/judge/pt/problems/view/1179
	
	
	Neste problema voc� dever� ler 15 valores coloc�-los em 2 vetores 
	conforme estes valores forem pares ou �mpares. S� que o tamanho de 
	cada um dos dois vetores � de 5 posi��es. Ent�o, cada vez que um dos 
	dois vetores encher, voc� dever� imprimir todo o vetor e utiliz�-lo 
	novamente para os pr�ximos n�meros que forem lidos. Terminada a 
	leitura, deve-se imprimir o conte�do que restou em cada um dos dois 
	vetores, imprimindo primeiro os valores do vetor impar. Cada vetor 
	pode ser preenchido tantas vezes quantas for necess�rio.

	Entrada
	A entrada cont�m 15 n�meros inteiros.
	
	Sa�da
	Imprima a sa�da conforme o exemplo abaixo.
*/

#include <iostream>
 
using namespace std;

void imprimirVetorPar(int vetor[], int qtd);
void imprimirVetorImpar(int vetor[], int qtd);

int main() {
    
    int valor, par[5], impar[5], contPar = 0, contImpar = 0;
    
    for (int i = 0; i < 15; i++) {
    	scanf("%d", &valor);
    	if (valor % 2 == 0) {
    		par[contPar] = valor;
    		contPar++;
    		if (contPar == 5) {
    			imprimirVetorPar(par, contPar);
    			contPar = 0;
			}
		} else {
    		impar[contImpar] = valor;
    		contImpar++;
    		if (contImpar == 5) {
    			imprimirVetorImpar(impar, contImpar);
    			contImpar = 0;
			}

		}
	}
	
	imprimirVetorImpar(impar, contImpar);
	imprimirVetorPar(par, contPar);
    
    return 0;
}


void imprimirVetorPar(int vetor[], int qtd) {
	for (int i=0; i < qtd; i++) {
		printf("par[%d] = %d\n", i, vetor[i]);
	}
}

void imprimirVetorImpar(int vetor[], int qtd) {
	for (int i=0; i < qtd; i++) {
		printf("impar[%d] = %d\n", i, vetor[i]);
	}
}
