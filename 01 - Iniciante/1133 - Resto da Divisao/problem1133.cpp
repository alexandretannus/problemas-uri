#include <iostream>

using namespace std;

int main() {

    int num1, num2, maior, menor;
    cin >> num1;
    cin >> num2;

    maior = num1 > num2 ? num1 : num2;
    menor = num1 < num2 ? num1 : num2;

    for (int num = menor+1; num < maior; num++) {
        if (num % 5 == 2 || num % 5 == 3) {
            cout << num << endl;
        }
    }
}