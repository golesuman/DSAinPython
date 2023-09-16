import collections


def valid_sudoku(board):
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    squares = collections.defaultdict(set)
    for i in range(len(board)):
        for j in range(len(board)):
            if (
                    board[i][j] in rows[i]
                    or board[i][j] in columns[j]
                    or board[i][j] in squares[(i // 3, j // 3)]
            ):
                return False
        rows[i].add(board[i][j])
        columns[j].add(board[i][j])
        squares[(i // 3, j // 3)].add(board[i][j])
    return True


arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(valid_sudoku(arr))
