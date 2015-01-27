DEBUG = TRUE
DEBUG_OPTIONS = -g
INCLUDES = -I . -I libs/
SOURCES= ${wildcard *.cpp}
OBJECTS = ${SOURCES:.cpp=.o}

all: ${OBJECTS}

%.o: %.cpp
	g++ ${INCLUDES} -g -c $< -o $@
clean:
	rm -f ${OBJECTS} 
