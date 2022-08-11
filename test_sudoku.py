from sudoku import *

# test ac3 updates cell values and only breaks when there are no new changes

# test easy puzzle
def test_easy_puzzle():
    '''
    This test requires only ac3 to solve, not backtrack
    '''
    puzzle = 'puzzle2.txt'
    solution = 'solutions/solution2.txt'
    grid = Sudoku_Grid(puzzle)
    solver = Sudoku_Solver(grid)
    solver.ac3()
    solution_grid = Sudoku_Grid(solution)
    solution_solved = Sudoku_Solver(solution_grid)
    assert(solver.cells == solution_solved.cells)


def test_intermediate_puzzle():
    """
    Req subset cover idea
    """
    puzzle = 'puzzle3.txt'
    solution = 'solutions/solution3.txt'
    grid = Sudoku_Grid(puzzle)
    solver = Sudoku_Solver(grid)
    solver.ac3()
    solution_grid = Sudoku_Grid(solution)
    solution_solved = Sudoku_Solver(solution_grid)
    assert(solver.cells == solution_solved.cells)