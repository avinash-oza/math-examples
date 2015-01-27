LIB = lib/
GTEST_DIR = ../../externals/google-test/
GTEST_INCLUDES = -I .
GTEST_OPTIONS = -isystem include/ -pthread
TEST_OPTIONS = -isystem ${GTEST_DIR}include/ -I ${GTEST_DIR} -pthread
TEST_INCLUDES = -I . -I ../${LIB}
SOURCES= ${wildcard *.cpp}
OBJECTS = ${SOURCES:.cpp=.o}
EXEC = test_runner

all: ${OBJECTS}
	g++ -I ${GTEST_DIR}/include -I ${GTEST_DIR} -pthread -c main.cpp -o main.o
	cd ../${LIB} && ${MAKE}
	g++ *.o ../${LIB}/*.o ${GTEST_DIR}libgtest.a -pthread -o test_runner
	./${EXEC}

%.o: %.cpp
	g++ ${TEST_INCLUDES} ${TEST_OPTIONS} -c $< -o $@

google-test:
	cd ${GTEST_DIR} && \
	g++ -I . -isystem include/ -pthread -c src/gtest-all.cc && \
	ar -rv libgtest.a gtest-all.o

clean:
	rm -f ${OBJECTS} ${EXEC}
