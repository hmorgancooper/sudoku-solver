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

    def __init__(self, puzzle):
        self.height = 9
        self.width = 9

        with open(puzzle) as f:
            contents = f.read().splitlines()
        
        self.squares = list()
        for i in range(self.height):
            for j in range(self.width):
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
        # with open(puzzle) as f:
        #    contents = f.read().splitlines()
        self.cells = {}
        self.domains = {}
        for cell in self.grid.squares:
            self.cells[(cell.i, cell.j)] = cell.value
            self.domains[(cell.i, cell.j)] = cell.domain

        
    def ac3(self):
        print(self.cells)
        # make cell row consistent
        # make cell column consistent
        # make cell block consistent
        print(stop)



def main():
    puzzle = 'puzzle1.txt'
    grid = Sudoku_Grid(puzzle)
    solver = Sudoku_Solver(grid)
    solver.ac3()
    
    print('stop')



if __name__ == "__main__":
    main()