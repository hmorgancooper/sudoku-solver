# sudoku-solver
Script  to solve sudoku puzzles! Puzzles are first filled in using logic until guess-work is necessary, then backtrack search is used to complete the puzzle. 

## Set up
Clone repo and set up venv.
Install requirements using
```bash
  pip install -r requirements.txt
```

The tests are run using pytest as follows:
```bash
  pytest test_sudoku.py
```

To run:
```bash
python3 sudoku.py
```

## Summary
* sudoku_board.py contains the class Sudoku_Board which is used to read in puzzles from text files and store the initial board state.
* sudoku.py contains the class Sudoku_Solver which takes the initial board as input, solves it, and then prints the final board state.


1. For each empty cell on the board the domain (set of possible values) is calculated and stored in Sudoku_Solver.domains 
2. Sudoku_Solver.fill_in_with_logic then recursively fills in board using the constraints that no number can be repeated
        in each row, column or block. Values already in row, col and block are removed
        from each cells domain. When there is only one value left in the domain, it is 
        added to the cell. When no new changes are made it is necessary to fill in the puzzle by guessing values for the cells.
3. Sudoku_Solver.backtrack_solve is then called which fills in the board using backtrack search. Backtrack search chooses values for the remaining cells until the constraints are broken, at which point it returns to the last choice and choses another option. This continues until the puzzle is complete.        



