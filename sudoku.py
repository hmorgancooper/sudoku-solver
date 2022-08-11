"""
File containing classes Sudoku_Grid and Square
"""

class Square():
    def __init__(self, i, j, value=None):
        self.i = i
        self.j = j
        self.value = value
        self.domain = set(range(1,10))
    

    def __str__(self):
        return f"({self.i}, {self.j}), {self.value}"
    

    def __eq__(self):
        return (
            (self.i == other.i) and
            (self.j == other.j))


class Sudoku_Grid():
    # get list of cell coordinates for each of the 3x3 blocks
    block1 = set()
    for i in range(1,4):
        for j in range(1,4):
            block1.add((i,j))
    block2 = set()
    for i in range(4, 7):
        for j in range(1,4):
            block2.add((i,j))
    block3 = set()
    for i in range(7, 10):
        for j in range(1,4):
            block3.add((i,j))
    
    block4 = set()
    for i in range(1,4):
        for j in range(4,7):
            block4.add((i,j))
    block5 = set()
    for i in range(4, 7):
        for j in range(4,7):
            block5.add((i,j))
    block6 = set()
    for i in range(7, 10):
        for j in range(4,7):
            block6.add((i,j))
    

    block7 = set()
    for i in range(1,4):
        for j in range(7,10):
            block7.add((i,j))
    block8 = set()
    for i in range(4, 7):
        for j in range(7,10):
            block8.add((i,j))
    block9 = set()
    for i in range(7, 10):
        for j in range(7,10):
            block9.add((i,j))

    def __init__(self, puzzle):
        self.height = 9
        self.width = 9

        with open(puzzle) as f:
            contents = f.read().splitlines()
        
        self.squares = list()
        for i in range(self.height):
            for j in range(self.width):
                if contents[i][j] != ".":
                    self.squares.append(Square(i+1, j+1, int(contents[i][j]))) 
                else:
                    self.squares.append(Square(i+1, j+1, contents[i][j]))

        
    
    def print(self):
        for item in self.squares:
            print(item.value, end=" ")
            if item.j == 9:
                print("")


class Sudoku_Solver():

    def __init__(self, grid):
        self.grid = grid
        self.height = self.grid.height
        self.width = self.grid.width

        # get dict of squares with corresponding values 
        # and separate dictionary of domains
        self.cells = {}
        self.domains = {}
        for cell in self.grid.squares:
            self.cells[(cell.i, cell.j)] = cell.value
            self.domains[(cell.i, cell.j)] = cell.domain

        
    def ac3(self):
        change_made = False
        for cell in self.cells:
            # only check unassigned cells
            if self.cells[cell] == '.':
                values_to_remove = self.find_inconsistent_values(cell) 
                for val in values_to_remove:
                    if val in self.domains[cell]:
                        self.domains[cell].remove(val)
                        change_made = True
                        if len(self.domains[cell]) == 0:
                            return False
                if len(self.domains[cell]) == 1:
                    self.cells[cell] = self.domains[cell]
        if change_made == True:
            self.ac3()
        else:
            return                
    

    def find_inconsistent_values(self, cell):
        # make cell consistent
        row_values = self.get_row_values(cell)
        col_values = self.get_col_values(cell)
        # make cell block consistent
        block_values = self.get_block_values(cell)
        remove_values = row_values.union(col_values)
        remove_values = remove_values.union(block_values)
        return remove_values


    def get_row_values(self, cell):
        """
        return set of cell values within the cell's row
        """
        row_num = cell[0]
        set_values = set()
        for i in range (1,10):
            set_values.add(self.cells[row_num, i])
        set_values.remove(".")
        return set_values


    def get_col_values(self, cell):
        """
        return set of cells within the cell's column
        """
        col_num = cell[1]
        set_values = set()
        for i in range (1,10):
            set_values.add(self.cells[i, col_num])
        set_values.remove(".")
        return set_values


    def get_block_values(self, cell):
        """
        return set of cells within the cell's block
        """
        i = cell[0]
        j = cell[1]

        if i < 4 and j < 4:
            block = self.grid.block1
        elif (i >= 4 and i < 7) and j < 4:
            block = self.grid.block2
        elif (i >= 7) and j < 4:
            block = self.grid.block3 

        elif i < 4 and (j >= 4 and j < 7):
            block = self.grid.block4
        elif (i >= 4 and i < 7) and (j >= 4 and j < 7):
            block = self.grid.block5
        elif (i >= 7) and (j >= 4 and j < 7):
            block = self.grid.block6

        elif i < 4 and j >= 7:
            block = self.grid.block7
        elif (i >= 4 and i < 7) and j >= 7:
            block = self.grid.block8
        elif (i >= 7) and j >= 7:
            block = self.grid.block9

        set_values = set()
        for cell in block:
            set_values.add(self.cells[cell])
        set_values.remove('.')
        return set_values
        






def main():
    puzzle = 'puzzle1.txt'
    grid = Sudoku_Grid(puzzle)
    solver = Sudoku_Solver(grid)
    solver.ac3()
    
    print('stop')



if __name__ == "__main__":
    main()