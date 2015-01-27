DEBUG = TRUE
DEBUG_OPTIONS = -g
LIBS = lib/
INCLUDES = -I . -I ${LIBS}
SOURCES= ${wildcard *.cpp}
OBJECTS = ${SOURCES:.cpp=.o}
EXEC = main_program

all: ${OBJECTS}
	cd lib/ && ${MAKE}
	g++ ${INCLUDES} -c main.cpp -o main.o
	g++ main.o ${LIBS}/*.o  -o ${EXEC}
tests: 
	cd test/ && $(MAKE)

clean:
	rm -f ${OBJECTS} ${EXEC}
	cd lib/ && ${MAKE} clean
	cd test/ && $(MAKE) clean
