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



def main():
    puzzle = 'puzzle1.txt'
    grid = Sudoku_Grid(puzzle)
    grid.print()
    print('stop')



if __name__ == "__main__":
    main()