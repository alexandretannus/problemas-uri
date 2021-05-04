#include <stdio.h>

int main() {

    int cx, cy, cz, nx, ny, nz, t;

    scanf("%d %d %d", &cx, &cy, &cz);
    scanf("%d %d %d", &nx, &ny, &nz);

    t = (nx/cx) * (ny/cy) * (nz/cz);

    printf("%d\n", t);

    return 0;
}
