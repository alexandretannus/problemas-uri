/*
	URI Online Judge
	Problema 1179 - Preenchimento de Vetor IV
	https://www.urionlinejudge.com.br/judge/pt/problems/view/1179
	
	
	Neste problema você deverá ler 15 valores colocá-los em 2 vetores 
	conforme estes valores forem pares ou ímpares. Só que o tamanho de 
	cada um dos dois vetores é de 5 posições. Então, cada vez que um dos 
	dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo 
	novamente para os próximos números que forem lidos. Terminada a 
	leitura, deve-se imprimir o conteúdo que restou em cada um dos dois 
	vetores, imprimindo primeiro os valores do vetor impar. Cada vetor 
	pode ser preenchido tantas vezes quantas for necessário.

	Entrada
	A entrada contém 15 números inteiros.
	
	Saída
	Imprima a saída conforme o exemplo abaixo.
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
