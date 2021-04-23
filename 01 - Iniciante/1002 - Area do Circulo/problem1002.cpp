/*  
	URI Online Judge 
	Problema 1002 - Área do Círculo
    https://www.urionlinejudge.com.br/repository/UOJ_1002.html
*/

#include <iostream>
 
using namespace std;
 
int main() {
 
    double pi = 3.14159;
	double R, A;
	
    scanf("%lf", &R),
    
    A = pi * R *R;
    
    printf("A=%.4lf\n", A);
 
    return 0;
}