CC = g++
CFLAGS = -g -Wall

clean:
	- rm -f *.o
	- rm sudoku_solver

# compile rules
sudoku_solver.o: sudoku.cpp
	$(CC) $(CFLAGS) -o $@ -c $^

sudoku_solver: sudoku_solver.o
	$(CC) $(CFLAGS) -o sudoku_solver sudoku_solver.o
