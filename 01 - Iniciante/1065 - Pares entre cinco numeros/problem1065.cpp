/*  
	URI Online Judge 
	Problema 1065 - Pares entre Cinco Números
    https://www.urionlinejudge.com.br/repository/UOJ_1065.html
*/

#include <iostream>
 
using namespace std;
 
int main() {
    int num, par = 0;
 
    for (int i=0; i<5; i++) {
        cin >> num;
        if (num % 2 == 0) {
            par++;
        }
    }
    
    cout << par << " valores pares" << endl;
 
    return 0;
}