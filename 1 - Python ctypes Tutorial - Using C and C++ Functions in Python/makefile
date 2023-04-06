CC=g++

all:
	$(CC) $(CFLAGS) -c -fPIC -o clib.o clib.cpp
	$(CC) $(CFLAGS) -fPIC -shared -o clib.so clib.o
	rm -f *.o

clean:
	rm -f *.o *.so