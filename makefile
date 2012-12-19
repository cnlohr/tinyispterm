TARGET=tinyispterm
INCLUDE=
LIB=-lusb
CFLAGS=-g -I.
OBJS=

all : $(TARGET)

tinyispterm : tinyispterm.o
	g++ -o $@ $^ $(LIB)

install : tinyispterm
	sudo cp tinyispterm /usr/local/bin/
	sudo cp 45-tinyisp.rules /etc/udev/rules.d/

clean :
	rm $(OBJS) *~ *.o $(TARGET) -rf
