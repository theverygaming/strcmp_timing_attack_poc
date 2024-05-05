#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

long nsdiff(struct timespec *start, struct timespec *end) {
    return (end->tv_nsec - start->tv_nsec) + ((end->tv_sec - start->tv_sec) * 1000000000l);
}

float get_latency(size_t sz, int it) {
    long long ns_total = 0;
    for (int i = 0; i < it; i++) {
        volatile uint8_t *buf_1 = malloc(sz);
        volatile uint8_t *buf_2 = malloc(sz);
        volatile uint8_t *buf_3 = malloc(sz);

        for (size_t i = 0; i < sz; i++) {
            buf_1[i] = rand();
        }

        for (size_t i = 0; i < sz; i++) {
            buf_2[i] = rand() % sz;
        }

        struct timespec tstart;
        clock_gettime(CLOCK_REALTIME, &tstart);

        for (size_t i = 0; i < sz; i++) {
            buf_3[buf_2[i]] = buf_1[buf_2[i]];
        }

        struct timespec tend;
        clock_gettime(CLOCK_REALTIME, &tend);

        free((uint8_t *)buf_1);
        free((uint8_t *)buf_2);
        free((uint8_t *)buf_3);

        ns_total += nsdiff(&tstart, &tend);
    }
    return ((float)ns_total / (float)it) / (float)sz;
}

int main() {
    srand(time(NULL));
    size_t sz = 64;
    for(int i = 0; i < 22; i++) {
        float latency = get_latency(sz, 10);
        printf("%zu,%f\n", sz, latency);
        fflush(stdout);

        sz <<= 1;
    }
}
