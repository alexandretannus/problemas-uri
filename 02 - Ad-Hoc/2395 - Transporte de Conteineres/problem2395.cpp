#include <iostream>

using namespace std;

int main() {

    int cx, cy, cz, nx, ny, nz;

    cin >> cx >> cy >> cz;
    cin >> nx >> ny >> nz;

    cout << (nx/cx) * (ny/cy) * (nz/cz) << endl; 

    return 0;
}
