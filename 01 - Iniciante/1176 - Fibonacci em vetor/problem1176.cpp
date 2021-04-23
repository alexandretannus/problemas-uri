/*
	URI Online Judge 
	Problema 1176 - Fibonacci em Vetor
	
	Fa�a um programa que leia um valor e apresente o n�mero de Fibonacci 
	correspondente a este valor lido. Lembre que os 2 primeiros elementos 
	da s�rie de Fibonacci s�o 0 e 1 e cada pr�ximo termo � a soma dos 2 
	anteriores a ele. Todos os valores de Fibonacci calculados neste problema 
	devem caber em um inteiro de 64 bits sem sinal.
	
	Entrada
	A primeira linha da entrada cont�m um inteiro T, indicando o n�mero de casos 
	de teste. Cada caso de teste cont�m um �nico inteiro N (0 <= N <= 60), 
	correspondente ao N-esimo termo da s�rie de Fibonacci.
	
	Sa�da
	Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X 
	� o N-�simo termo da s�rie de Fibonacci.
*/

#include <iostream>
 
using namespace std;
 
int main() {
 
    long long int fibo[61];
	int t, n;
    fibo[0] = 0;
    fibo[1] = 1;
    
    for (int i=2; i<61; i++) {
    	fibo[i] = fibo[i-1] + fibo[i-2];
	}
	
	scanf("%d", &t);
	 
	for (int j=0; j<t; j++){
		scanf("%d", &n);
		printf("Fib(%d) = %lld\n", n, fibo[n]);
	}
 
    return 0;
}

