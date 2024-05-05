CFLAGS = -O3 -I . -Wall -Wextra -Werror

.PHONY: all
all: latency

run: latency
	./latency | tee out.csv

plot:
	gnuplot -e "set term png; set output 'plot.png'; set datafile separator ','; set logscale x; \
	set xlabel \"size\"; \
	set ylabel \"latency (ns)\"; \
	set xtics 64,2 add ( \
	\"1k\" 1024, \
	\"2k\" 2048, \
	\"4k\" 4096, \
	\"8k\" 8192, \
	\"16k\" 16384, \
	\"32k\" 32768, \
	\"64k\" 65536, \
	\"128k\" 131072, \
	\"256k\" 262144, \
	\"512k\" 524288, \
	\"1M\" 1048576, \
	\"2M\" 2097152, \
	\"4M\" 4194304, \
	\"8M\" 8388608, \
	\"16M\" 16777216, \
	\"32M\" 33554432, \
	\"64M\" 67108864, \
	\"128M\" 134217728, \
	\"256M\" 268435456, \
	\"512M\" 536870912) rotate by 45 right; \
	set xrange [64:*]; plot 'out.csv' using 1:2 with line"

latency: latency.o
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

clean:
	rm -f latency.o
	rm -f latency
	rm -f out.csv plot.png
