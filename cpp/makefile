DEBUG = TRUE
DEBUG_OPTIONS = -g
BISECT_COMMANDS = -I . -c bisect.cpp

all: bisect.o
ifeq (${DEBUG},TRUE)
	g++ bisect.o ${DEBUG_OPTIONS} -o bisect
else
	g++ bisect.o -o bisect
endif
bond_pv: bond_pv.h bond_pv.cpp
	g++ bond_pv.cpp -o bond_pv
bisect.o: bisect.cpp bisect.h
	g++ -I . -c bisect.cpp
tests: 
	cd test/ && $(MAKE)
clean:
	rm -Rf *.o
	rm -Rf bisect
    
    
    
