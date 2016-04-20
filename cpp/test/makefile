LIB = lib/
SRC = src/
GTEST_DIR = ../../externals/google-test/
GTEST_INCLUDES = -I .
GTEST_OPTIONS = -isystem include/ -pthread
TEST_OPTIONS = -isystem ${GTEST_DIR}include/ -I ${GTEST_DIR} -pthread
TEST_INCLUDES = -I . -I ../${LIB}
SOURCES= ${wildcard *.cc}
OBJECTS = ${SOURCES:.cc=.o}
EXEC = test_runner

#all: gtest-all.o ${OBJECTS}
#g++ -I ${GTEST_DIR}/include -I ${GTEST_DIR} -pthread -c main.cpp -o main.o
#cd ../${LIB} && ${MAKE}
#g++ *.o ../${LIB}/*.o ${GTEST_DIR}gtest-all.o -pthread -o test_runner
#./${EXEC}
all: google-test
	g++ -I ${GTEST_DIR}include -I ${GTEST_DIR} -pthread -c main.cpp -o main.o
	g++ *.o ../${LIB}/*.o  ${GTEST_DIR}gtest-all.o -pthread -o ${EXEC}
	./${EXEC}

%.o: %.cc
	g++ ${TEST_INCLUDES} ${TEST_OPTIONS} -c $< -o $@

gtest-all.o:
	cd ${GTEST_DIR}src && ${MAKE} gtest-all.o

google-test:
	cd ${GTEST_DIR} && \
	g++ -I . -isystem include/ -pthread -c src/gtest-all.cc && \
	ar -rv libgtest.a gtest-all.o

clean:
	rm -f ${OBJECTS} ${EXEC}
