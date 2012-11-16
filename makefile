TARGET=tinyispterm
INCLUDE=
LIB=-lusb
CFLAGS=-g -I.
OBJS=

all : $(TARGET)

tinyispterm : tinyispterm.o
	g++ -o $@ $^ $(LIB)

clean :
	rm $(OBJS) *~ *.o $(TARGET) -rf
