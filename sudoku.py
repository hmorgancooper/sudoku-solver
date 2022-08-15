import time 

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
                #self.add_if_candidate_unique(cell)
                values_to_remove = self.find_inconsistent_values(cell) 
                for val in values_to_remove:
                    if val in self.domains[cell]:
                        self.domains[cell].remove(val)
                        change_made = True
                        if len(self.domains[cell]) == 0:
                            return False
                if len(self.domains[cell]) == 1:
                     self.cells[cell] = min(self.domains[cell])
        if change_made == True:
            self.ac3()
        else:
            return 
               
    

    def find_inconsistent_values(self, cell):
        row_values = self.get_row_values(cell)
        col_values = self.get_col_values(cell)
        # make cell block consistent
        block_values = self.get_block_values(cell)
        remove_values = row_values.union(col_values)
        remove_values = remove_values.union(block_values)
        return remove_values
    

    # def find_inconsistent_values(self, cell):
    #     row_values = self.get_row_values(cell)
    #     if self.cells[cell] in row_values:
    #         return False
    #     col_values = self.get_col_values(cell)
    #     if self.cells[cell] in col_values:
    #         return False
    #     # make cell block consistent
    #     block_values = self.get_block_values(cell)
    #     if self.cells[cell] in block_values:
    #         return False
    #     else:
    #         return True
    #     remove_values = row_values.union(col_values)
    #     remove_values = remove_values.union(block_values)
    #     return remove_values


    # def get_row_values(self, cell):
    #     """
    #     return set of cell values within the cell's row
    #     """
    #     row_num = cell[0]
    #     set_values = set()
    #     for i in range (1,10):
    #         # don't include current cell
    #         if (row_num, i) != (cell[0], cell[1]):
    #             set_values.add(self.cells[row_num, i])
    #     return set_values
    
    def get_row_values(self, cell):
        row_values = {(cell[0], 1), (cell[0], 2), (cell[0], 3), (cell[0], 4), (cell[0], 5), (cell[0], 6),
                      (cell[0], 7), (cell[0], 8), (cell[0], 9)}
        row_values.remove((cell[0], cell[1]))
        set_values = set()
        for cell in row_values:
            set_values.add(self.cells[cell])
        return set_values


    # def get_col_values(self, cell):
    #     """
    #     return set of cells within the cell's column
    #     """
    #     col_num = cell[1]
    #     set_values = set()
    #     for i in range (1,10):
    #         if (i, col_num) != (cell[0], cell[1]):
    #             set_values.add(self.cells[i, col_num])
    #     return set_values
    
    def get_col_values(self, cell):
        col_values = {(1, cell[1]), (2, cell[1]), (3, cell[1]), (4, cell[1]), (5, cell[1]), (6, cell[1]),
                      (7, cell[1]), (8, cell[1]), (9, cell[1])}
        col_values.remove((cell[0], cell[1]))
        set_values = set()
        for cell in col_values:
            set_values.add(self.cells[cell])
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
        block_temp = block.copy()
        block_temp.remove(cell)
        for block_cell in block_temp:
            set_values.add(self.cells[block_cell])
        return set_values

        
    def backtrack_solve(self):
        if self.puzzle_complete():
            return
        cells = self.get_cell_list()
        cell = cells.pop()
        for val in self.domains[cell]:
            self.cells[cell] = val
            if self.is_cell_consistent(cell):
                self.backtrack_solve()
            if self.puzzle_complete() and self.is_consistent():
                return
            # delete last value
            self.cells[cell] = '.'
          
    def add_if_candidate_unique(self, cell):
        for val in self.domains[cell]:
               # get row domains: return if val not in domain
            row_num = cell[0]
            col_num = cell[1]
            row_domain_values = set()
            col_domain_values = set()
            for i in range (1,10):
                if (row_num, i) != (cell[0], cell[1]):
                    row_domain_values = row_domain_values.union(self.domains[row_num, i])
                    col_domain_values = col_domain_values.union(self.domains[i, col_num])
            if val not in row_domain_values:
                print('Not in domain!')
            if val not in col_domain_values:
                print('Not in domain!')
            

         # get col domains
         # get block domains
        return 
         
         
         

    def puzzle_complete(self):
        if '.' not in self.cells.values():
            return True
        else:
            return False
    
    def get_cell_list(self):
        vars = []
        for var in self.cells.keys():
            if self.cells[var] == '.':
                vars.append(var)
        vars.sort(key = lambda var: len(self.domains[var]), reverse = True)
        return vars
    
    def is_consistent(self):
        for cell in self.cells:
            if self.cells[cell] != '.':
                val = self.cells[cell]
                inconsistent_vals = self.find_inconsistent_values(cell)
                if self.cells[cell] in inconsistent_vals: 
                    return False
        return True

    
    def is_cell_consistent(self, cell):
        inconsistent_vals = self.find_inconsistent_values(cell)
        if self.cells[cell] in inconsistent_vals: 
            return False
        return True
    
    # def is_cell_consistent(self, cell):
    #     inconsistent_vals = self.find_inconsistent_values(cell)
    #     if inconsistent_vals == False: 
    #         return False
    #     return True
    
    def print():
        ...

        
def main():
    puzzle = 'puzzle4.txt'
    grid = Sudoku_Grid(puzzle)
    solver = Sudoku_Solver(grid)
    tic = time.perf_counter()
    solver.ac3()
    toc = time.perf_counter()
    solver.backtrack_solve()
    bong = time.perf_counter()
    
    #print(f"ac3 time is {tic - toc}")
    print(f"solver time is {bong - toc}")
    print(f'total time is {bong - tic}')
    print('stop')



if __name__ == "__main__":
    main()