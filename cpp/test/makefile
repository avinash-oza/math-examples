GTEST_DIR = ../../externals/google-test/
GTEST_INCLUDES = -I .
GTEST_OPTIONS = -isystem include/ -pthread
TEST_OPTIONS = -isystem ${GTEST_DIR}include/ -I ${GTEST_DIR} -pthread
SOURCES= ${wildcard *.cpp}
OBJECTS = ${SOURCES:.cpp=.o}
EXEC = test_runner
all: gtest ${OBJECTS}
	g++ -I ${GTEST_DIR}/include -I ${GTEST_DIR} -pthread -c main.cpp -o main.o
	g++ *.o ${GTEST_DIR}libgtest.a -pthread -o test_runner

%.o: %.cpp
	g++ ${TEST_OPTIONS} -c $< -o $@

gtest:
	cd ${GTEST_DIR} && \
	g++ -I . -isystem include/ -pthread -c src/gtest-all.cc && \
	ar -rv libgtest.a gtest-all.o

clean:
	rm -f ${OBJECTS} ${EXEC}
