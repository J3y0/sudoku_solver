HEIGHT = 9
WIDTH = 9

def init_grid():
    """
    Initialize the grid with zeros
    """
    grid = []
    for i in range(HEIGHT):
        L = []
        for j in range(WIDTH):
            L.append(0)
        grid.append(L)
    return grid

def init_possibilities():
    """
    Initialize the grid with zeros
    """
    grid = []
    for i in range(HEIGHT):
        L = []
        for j in range(WIDTH):
            L.append(list(range(1, 10)))
        grid.append(L)
    return grid

def print_grid(grid):
    """
    Print a pretty grid
    """
    print("||---|---|---||---|---|---||---|---|---||")
    for i in range(HEIGHT):
        print("||", end="")
        for j in range(WIDTH):
            if (j%3 == 2):
                print(" " + str(grid[i][j]) + " ||", end="")
            else:
                print(" " + str(grid[i][j]) + " |", end="")
        
        if (i%3 == 2):
            print("\n||---|---|---||---|---|---||---|---|---||")
        else:
            print("")

def check_grid(grid):
    """
    Check if the grid is valid or not (one digit per column, line and block)
    """
    pass

def lines(grid, possibilities):
    """
    Fill the possibilities for each cell, checking the lines

    The function directly modifies the possibilities parameter.
    """
    # Going through each line
    for i in range(HEIGHT):
        in_line = []
        for j in range(WIDTH):
            # For each non-zero cell value, we remove it from the possibilities
            # because it is on the line
            cell = grid[i][j]
            if cell != 0 and cell not in in_line:
                possibilities[i][j] = []
                # for k in range(WIDTH):
                #     if grid[i][j] in possibilities[i][k]:
                #         possibilities[i][k].remove(grid[i][j])
                in_line.append(cell)
        for j in range(WIDTH):
            for elt in in_line:
                if elt in possibilities[i][j]:
                    possibilities[i][j].remove(elt)


def columns(grid, possibilities):
    """
    Fill the possibilities for each cell, checking the columns.
    
    The function directly modifies the possibilities parameter.
    """
    # Going through each column
    for j in range(WIDTH):
        in_column = []
        for i in range(HEIGHT):
            # For each non-zero cell value, we remove it from the possibilities
            # because it is on the column
            cell = grid[i][j]
            if cell != 0 and cell not in in_column:
                possibilities[i][j] = []
                #     for k in range(HEIGHT):
                #         if cell in possibilities[k][j]:
                #             possibilities[k][j].remove(cell)
                in_column.append(cell)
        for i in range(HEIGHT):
            for elt in in_column:
                if elt in possibilities[i][j]:
                    possibilities[i][j].remove(elt)


def block(grid, possibilities):
    """
    Fill the possibilities for each cell, checking the blocks.
    
    The function directly modifies the possibilities parameter.
    """
    # Going through each block
    for n_block in range(9):
        in_block = []
        for line in range(3):
            for column in range(3):
                cell = grid[3*(n_block//3) + line][3*(n_block%3) + column]
                if cell != 0:
                    possibilities[3*(n_block//3) + line][3*(n_block%3) + column] = []
                    if cell not in in_block:
                        in_block.append(cell)
        for line in range(3):
            for column in range(3):
                for elt in in_block:
                    if elt in possibilities[3*(n_block//3) + line][3*(n_block%3) + column]:
                        possibilities[3*(n_block//3) + line][3*(n_block%3) + column].remove(elt)
                    


def fill(grid, possibilities):
    """
    Fill the grid with the only option when there is one (given by possibilities)
    """
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if len(possibilities[i][j]) == 1:
                grid[i][j] = possibilities[i][j][0]

def recurse_solve(grid):
    pass


if __name__ == "__main__":
    grid = init_grid()
    possibilities = init_possibilities()
    grid[0][0] = 5
    grid[0][2] = 1
    grid[0][3] = 2
    grid[0][4] = 3
    grid[0][5] = 4
    grid[0][6] = 7
    grid[0][7] = 8
    grid[0][8] = 9
    grid[4][2] = 4
    grid[6][6] = 8
    print_grid(grid)
    
    
    columns(grid, possibilities)
    lines(grid, possibilities)
    block(grid, possibilities)
    fill(grid, possibilities)
    print_grid(grid)


    # Objective: coding an optimized algorithm
    # where it first uses non-recursive algo and if 
    # there is an infinite loop, then, call the recursive one
