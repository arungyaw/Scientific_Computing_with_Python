class Board:
    def __init__(self, board):
        self.board = board

#Convert list items into string
    def __str__(self):
        board_str = ''
        for row in self.board:
            row_str = [str(i) if i else '*' for i in row]
            board_str += ' '.join(row_str)
            board_str += '\n'
        return board_str

#Find empty cells with value 0
    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

#Find number existing in asked row
    def valid_in_row(self, row, num):
        return num not in self.board[row]

#Find number existing in asked column
    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

#Find number existing in asked square(col*row)
    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

#To check if the number is valid or not
    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

#Solver
    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False

#Print function
def solve_sudoku(board):
    gameboard = Board(board)
    print(f'Puzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print(f'Solved puzzle:\n{gameboard}')
    else:
        print('The provided puzzle is unsolvable.')
    return gameboard

puzzle = [
  [0, 0, 4, 1, 0, 8, 0, 9, 0],
  [0, 6, 1, 0, 0, 3, 4, 0, 0],
  [0, 0, 0, 0, 6, 5, 2, 3, 0],
  [7, 0, 0, 0, 5, 1, 0, 6, 2],
  [2, 0, 3, 0, 0, 0, 1, 0, 8],
  [6, 0, 0, 3, 2, 0, 0, 0, 5],
  [0, 9, 2, 7, 3, 0, 0, 0, 4],
  [0, 0, 5, 9, 0, 0, 6, 1, 0],
  [0, 3, 0, 5, 0, 4, 7, 0, 0]
]

solve_sudoku(puzzle)