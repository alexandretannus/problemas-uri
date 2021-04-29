/*  
	URI Online Judge 
	Problema 1094 - Experiencias
    https://www.urionlinejudge.com.br/repository/UOJ_1080.html 
 */

#include <iostream>
#include <iomanip> 

using namespace std;

int main() {

    int casos, qtdInput, qtdSapos = 0, qtdCoelhos = 0, qtdRatos = 0, total;
    char tipo;
    
    cin >> casos;

    for (int i=0; i<casos; i++){
        cin >> qtdInput >> tipo;
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

    cout << "Total: " << total << " cobaias" << endl;
    cout << "Total de coelhos: " << qtdCoelhos << endl;
    cout << "Total de ratos: " << qtdRatos << endl;
    cout << "Total de sapos: " << qtdSapos << endl;
    cout << fixed << setprecision(2);
    cout << "Percentual de coelhos: " << 100.0 * qtdCoelhos / total << " %" << endl;
    cout << "Percentual de ratos: " << 100.0 * qtdRatos / total << " %" << endl;
    cout << "Percentual de sapos: " << 100.0 * qtdSapos / total << " %" << endl;
        
    return 0;
}
