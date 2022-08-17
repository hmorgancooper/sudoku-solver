"""
This file contains the classes for the sudoku board and for each sudoku square
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


class Sudoku_Board():
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