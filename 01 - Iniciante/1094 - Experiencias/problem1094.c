/*  
	URI Online Judge 
	Problema 1094 - Experiencias
    https://www.urionlinejudge.com.br/repository/UOJ_1080.html 
 */

 #include <stdio.h>

 int main() {

    int casos, qtdInput, qtdSapos = 0, qtdCoelhos = 0, qtdRatos = 0, total = 0, i;
    char tipo;

	scanf("%d", &casos);

    for (i=0; i<casos; i++){
        scanf("%d %c", &qtdInput, &tipo);
        
        total += qtdInput;

        switch(tipo) {
            case 'R': 
                qtdRatos += qtdInput;
                break;
            case 'S': 
                qtdSapos += qtdInput;
                break;
            case 'C': 
                qtdCoelhos += qtdInput;
                break;
        }

    }

    printf("Total: %d cobaias\n", total);
    printf("Total de coelhos: %d\n", qtdCoelhos);
    printf("Total de ratos: %d\n", qtdRatos);
    printf("Total de sapos: %d\n", qtdSapos);
    printf("Percentual de coelhos: %.2f %\n", 100.0 * qtdCoelhos / total);
    printf("Percentual de ratos: %.2f %\n", 100.0 * qtdRatos / total);
    printf("Percentual de sapos: %.2f %\n", 100.0 * qtdSapos / total);
     
    return 0;
 }
