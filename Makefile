LIBS=-lcsfml-graphics -lcsfml-window -lcsfml-system
CC=gcc
LIB_CC=$(CC) -c -Wall -Werror -fPIC -O2

UTILS=./src/utils.h
DRAW=./src/draw.h ./src/draw.c
RESOURCES=./src/resources.h ./src/resources.c

FILES=$(UTILS) $(DRAW) $(RESOURCES)

all:
	@echo "** Building library"
	@mkdir -p ./build
	@cp -r ./src/res ./build
	gcc -Wall -O2 $(FILES) ./src/main.c -o ./build/main $(LIBS)

lib:
	@echo "** Building Shared Library"
	@mkdir -p build/objs
	$(LIB_CC) ./src/draw.c -o ./build/objs/draw.o
	$(LIB_CC) ./src/resources.c -o ./build/objs/ressources.o
	$(CC) -shared $(LIBS) ./build/objs/* -o ./build/bdl.so
	@rm -rf ./build/objs

clean:
	@echo "** Cleaning"
	@rm -fr build
