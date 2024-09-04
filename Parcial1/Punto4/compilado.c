#include <stdio.h>
#include <time.h>

int main() {
    long long int sum = 0;
    clock_t start, end;

    start = clock();
    for (long long int i = 1; i <= 10000000; i++) {
        sum += i;
    }
    end = clock();

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC;
    printf("Suma: %lld\n", sum);
    printf("Tiempo tomado: %f segundos\n", time_taken);

    return 0;
}
