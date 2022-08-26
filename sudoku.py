from sudoku_board import *
import sys

class Sudoku_Solver():

    def __init__(self, grid):
        self.grid = grid
        self.height = self.grid.height
        self.width = self.grid.width
        self.cells = {}
        self.domains = {}
        for cell in self.grid.squares:
            self.cells[(cell.i, cell.j)] = cell.value
            self.domains[(cell.i, cell.j)] = cell.domain

        
    def fill_in_with_logic(self):
        """
        Recursively fills in board using constraints that no number can be repeated
        in each row, column or block. Values already in row, col and block are removed
        from each cells domain. When there is only one value left in the domain, it is 
        added to the cell.
        """
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
                            sys.exit("Domain empty, impossible puzzle!")
                            return False
                if len(self.domains[cell]) == 1:
                     self.cells[cell] = min(self.domains[cell])
        if change_made == True:
            self.fill_in_with_logic()
        else:
            return 
      

    def find_inconsistent_values(self, cell):
        """
        Finds values that must be removed from the domain of the cell
        """
        row_values = self.get_row_values(cell)
        col_values = self.get_col_values(cell)
        # make cell block consistent
        block_values = self.get_block_values(cell)
        remove_values = row_values.union(col_values)
        remove_values = remove_values.union(block_values)
        return remove_values

    
    def get_row_values(self, cell):
        row_values = {(cell[0], 1), (cell[0], 2), (cell[0], 3), (cell[0], 4), (cell[0], 5), (cell[0], 6),
                      (cell[0], 7), (cell[0], 8), (cell[0], 9)}
        row_values.remove((cell[0], cell[1]))
        set_values = set()
        for cell in row_values:
            set_values.add(self.cells[cell])
        return set_values

    
    def get_col_values(self, cell):
        col_values = {(1, cell[1]), (2, cell[1]), (3, cell[1]), (4, cell[1]), (5, cell[1]), (6, cell[1]),
                      (7, cell[1]), (8, cell[1]), (9, cell[1])}
        col_values.remove((cell[0], cell[1]))
        set_values = set()
        for cell in col_values:
            set_values.add(self.cells[cell])
        return set_values


    def get_block_values(self, cell):
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


    def backtrack_solve(self, empty_cells=None):
        """
        Fills in board using backtrack search
        """
        if empty_cells == None:
            empty_cells = self.get_cell_list()
        if self.puzzle_complete(empty_cells):
            return
        cell = empty_cells.pop()
        for val in self.domains[cell]:
            self.cells[cell] = val
            if self.is_cell_consistent(cell):
                self.backtrack_solve(empty_cells)
            if self.puzzle_complete(empty_cells) and self.is_consistent():
                return
            # delete last value
            self.cells[cell] = '.'
        empty_cells.append(cell)

        
    def puzzle_complete(self, empty_cells):
        if len(empty_cells) == 0:
            return True
        else:
            return False
    
    def get_cell_list(self):
        """
        Gets list of empty cells and sorts them in order of domain size (smallest domain -> chosen first)
        """
        vars = []
        for var in self.cells.keys():
            if self.cells[var] == '.':
                vars.append(var)
        vars.sort(key = lambda var: len(self.domains[var]), reverse = True)
        return vars
    
    def is_consistent(self):
        """
        Checks if board is consistent (breaks no constraints)
        """
        for cell in self.cells:
            if self.is_cell_consistent(cell) == False:
                return False
        return True

    
    def is_cell_consistent(self, cell):
        """
        Checks if cell is consistent
        """
        row_values = self.get_row_values(cell)
        if self.cells[cell] in row_values:
            return False
        col_values = self.get_col_values(cell)
        if self.cells[cell] in col_values:
            return False
        # make cell block consistent
        block_values = self.get_block_values(cell)
        if self.cells[cell] in block_values:
            return False
        else:
            return True
    
    
    def print(self):
        for cell in self.cells.keys():
            print(self.cells[cell], end=" ")
            if cell[1] == 3 or cell[1] == 6:
                print(" ", end="")
            if cell[1]/9 == 1:
                print("")
            if (cell[0] in [3,6]) and cell[1] == 9:
                print("\n", end = "")
        return None      


    def solve(self, solver):
        solver.fill_in_with_logic()
        print("\nSolving...")
        solver.backtrack_solve()
        print("\nFinished board!\n")
        solver.print()


def main():
    if len(sys.argv) != 2:
        sys.exit("Command line input must be in form: python3 sudoku.py [puzzle_file.txt]")

    puzzle = "puzzles/" + sys.argv[1]
    board = Sudoku_Board(puzzle)
    solver = Sudoku_Solver(board)
    print("Initial board:\n")
    solver.print()
    solver.solve(solver)
    


if __name__ == "__main__":
    main()