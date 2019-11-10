LIBS=-lcsfml-graphics -lcsfml-window -lcsfml-system
CC=gcc
LIB_CC=$(CC) -c -Wall -O2
LIB_CC_SHARED=$(CC) -c -Wall -Werror -fPIC -O2

UTILS=./src/utils.h ./src/utils.c
DRAW=./src/draw.h ./src/draw.c
RESOURCES=./src/resources.h ./src/resources.c

FILES=$(UTILS) $(DRAW) $(RESOURCES)

all:
	@echo "** Building library"
	@mkdir -p ./build
	@cp -r ./src/res ./build
	$(LIB_CC) $(FILES) ./src/main.c -o ./build/main $(LIBS)

lib:
	@echo "** Building Shared Library"
	@mkdir -p build/objs
	$(LIB_CC_SHARED) ./src/utils.c -o ./build/objs/utils.o
	$(LIB_CC_SHARED) ./src/draw.c -o ./build/objs/draw.o
	$(LIB_CC_SHARED) ./src/resources.c -o ./build/objs/ressources.o
	$(CC) -shared ./build/objs/* -o ./build/bdl.so $(LIBS)
	@rm -rf ./build/objs

clean:
	@echo "** Cleaning"
	@rm -fr build
