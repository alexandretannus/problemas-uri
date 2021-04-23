/*  
	URI Online Judge 
	Problema 2342 - Overflow
    https://www.urionlinejudge.com.br/repository/UOJ_2342.html
*/

#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;
 
int main() {

	int n, a, b, total;
	string op;
	
	cin >> n;
	cin >> a >> op >> b;
	
	
	if (op == "+") {
		total = a + b;
	} else {
		total = a * b;
	}
	
	if (total > n) {
		cout << "OVERFLOW" << endl;
	} else {
		cout << "OK" << endl;
	}
	 
    return 0;
}