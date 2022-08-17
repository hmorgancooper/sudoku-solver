from sudoku import *

# test ac3 updates cell values and only breaks when there are no new changes

# test easy puzzle
def test_easy_puzzle():
    '''
    This test requires only filling with logic to solve, not backtrack
    '''
    puzzle = 'puzzles/puzzle1.txt'
    solution = 'solutions/solution1.txt'
    grid = Sudoku_Board(puzzle)
    solver = Sudoku_Solver(grid)
    solver.fill_in_with_logic()
    solution_grid = Sudoku_Board(solution)
    solution_solved = Sudoku_Solver(solution_grid)
    assert(solver.cells == solution_solved.cells)


def test_intermediate_puzzle():
    """
    Puzzle requires logic and backtrack
    """
    puzzle = 'puzzles/puzzle2.txt'
    solution = 'solutions/solution2.txt'
    grid = Sudoku_Board(puzzle)
    solver = Sudoku_Solver(grid)
    solver.fill_in_with_logic()
    solver.backtrack_solve()
    solution_grid = Sudoku_Board(solution)
    solution_solved = Sudoku_Solver(solution_grid)
    assert(solver.cells == solution_solved.cells)

def test_hard_puzzle():
    puzzle = 'puzzles/puzzle3.txt'
    solution = 'solutions/solution3.txt'
    grid = Sudoku_Board(puzzle)
    solver = Sudoku_Solver(grid)
    solver.fill_in_with_logic()
    solver.backtrack_solve()
    solution_grid = Sudoku_Board(solution)
    solution_solved = Sudoku_Solver(solution_grid)
    assert(solver.cells == solution_solved.cells)



 