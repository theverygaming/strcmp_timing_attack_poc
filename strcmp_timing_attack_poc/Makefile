CFLAGS = -O3 -I . -Wall -Wextra -Werror

.PHONY: all
all: timingpoc

run: timingpoc
	./timingpoc

timingpoc: strcmp.o secret.o exploit.o
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

clean:
	rm -f strcmp.o secret.o exploit.o
	rm -f timingpoc
