
#include <iostream>
 
using namespace std;

int main() {
 
    int  a[100001], s1 = 0, s2 = 0, tam;
 	long n, ind;
 	cin >> n;

	for (long int i=0; i<n; i++) {
		cin >> a[i];
		s1 += a[i];
	}
	
	tam = s1/2;
	for (ind=0; ind<n; ind++) {
		s2 += a[ind];
		if (s2 == tam) {
		    break;
		}
	}
	
	cout << ind+1 << endl;
	  
    return 0;
}
