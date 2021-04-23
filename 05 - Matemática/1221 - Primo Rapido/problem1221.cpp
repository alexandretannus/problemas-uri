/*
    
	URI Online Judge 
	Problema 1121 - Primo Rápido

    Mariazinha sabe que um Número Primo é aquele que pode ser dividido somente 
    por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser 
    dividido apenas pelo número 1 e pelo número 7 sem que haja resto. Então 
    ela pediu para você fazer um programa que aceite diversos valores e diga 
    se cada um destes valores é primo ou não. Acontece que a paciência não é 
    uma das virtudes de Mariazinha, portanto ela quer que a execução de todos 
    os casos de teste que ela selecionar (instâncias) aconteçam no tempo 
    máximo de um segundo, pois ela odeia esperar.

    Entrada
    A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 200), 
    correspondente ao número de casos de teste. Seguem N linhas, cada uma 
    contendo um valor inteiro X (1 < X < 2^31) que pode ser ou não, um número 
    primo.

    Saída
    Para cada caso de teste imprima a mensagem “Prime” (Primo) ou 
    “Not Prime” (Não Primo), de acordo com o exemplo abaixo.
    Exemplo de Entrada	
    3
    123321
    123
    103

    Exemplo de Saída
    Not Prime
    Not Prime
    Prime
*/

#include <iostream>
#include <cmath>
using namespace std;


int main() {
	
	int casos, num, divs = 0;
	
	scanf("%d", &casos);
	
	for (int i=0; i<casos; i++) {
		scanf("%d", &num);
		divs = 0;
		for (int j=2; j<int(sqrt(num))+1; j++) {
			if (num%j == 0) {
				divs++;
			}
		}
		if(divs == 0)
		{
			printf("Prime\n");			
		}
		else {
			printf("Not Prime\n");			
		}
			
	}
	
    return 0;
}
