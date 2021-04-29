#include <stdio.h>

int main() {

    int num1, num2, maior, menor;
    scanf("%d", &num1);
    scanf("%d", &num2);

    maior = num1 > num2 ? num1 : num2;
    menor = num1 < num2 ? num1 : num2;

    for (int num = menor+1; num < maior; num++) {
        if (num % 5 == 2 || num % 5 == 3) {
            printf("%d\n", num);
        }
    }
}