GTEST_DIR = ../../externals/google-test/
GTEST_INCLUDES = -I .
GTEST_OPTIONS = -isystem include/ -pthread

all: bisect_test
bisect_test: gtest
	g++ -isystem ${GTEST_DIR}include/ -I ${GTEST_DIR} \
		-pthread bisect_test.cpp ${GTEST_DIR}libgtest.a \
		-o bisect_test

gtest:
	cd ${GTEST_DIR} && \
	g++ ${GTEST_INCLUDES} ${GTEST_OPTIONS} -c src/gtest-all.cc && \
	ar -rv libgtest.a gtest-all.o


