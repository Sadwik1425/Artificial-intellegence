def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_8_queens(board):
    n = len(board)

    def place_queen(col):
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1

                if col == n - 1:
                    return True
                if place_queen(col + 1):
                    return True

                board[i][col] = 0
            elif board[i][col] == 1:
                break
        return False

    if not place_queen(0):
        return False

    print_board(board)
    return True

board = [[0]*8 for _ in range(8)]
solve_8_queens(board)
