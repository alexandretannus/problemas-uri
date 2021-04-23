/*  
	URI Online Judge 
	Problema 1051 - Imposto de Renda
    https://www.urionlinejudge.com.br/repository/UOJ_1051.html
*/

#include <stdio.h>

int main() {
    float renda, imposto=0;
    scanf("%f", &renda);

    if (renda >=0 && renda <= 2000 ) {
        printf("Isento\n");
        return 0;
    }
    
    if (renda > 2000 && renda <= 3000) {
        imposto = (renda - 2000) * 0.08;
    }
    
    if (renda > 3000 && renda <= 4500) {
        imposto = 1000 * 0.08 + (renda - 3000) * 0.18;        
    }

    if (renda > 4500) {
        imposto = 1000 * 0.08  + 1500 * 0.18 + (renda - 4500)*0.28;  
    }

    printf("R$ %.2f\n", imposto);
}

