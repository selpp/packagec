LIBS=-lcsfml-graphics -lcsfml-window -lcsfml-system

all:
	@echo "** Building library"
	@mkdir -p build
	gcc -Wall -O2 ./src/utils.h     \
								./src/draw.h      \
								./src/draw.c      \
								./src/resources.h \
								./src/resources.c \
								./src/main.c      \
								-o ./build/main $(LIBS)
