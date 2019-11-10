LIBS=-lcsfml-graphics -lcsfml-window -lcsfml-system

UTILS=./src/utils.h
DRAW=./src/draw.h ./src/draw.c
RESOURCES=./src/resources.h ./src/resources.c

FILES=$(UTILS) $(DRAW) $(RESOURCES)

all:
	@echo "** Building library"
	@mkdir -p ./build
	@cp -r ./src/res ./build
	gcc -Wall -O2 $(FILES) ./src/main.c -o ./build/main $(LIBS)
