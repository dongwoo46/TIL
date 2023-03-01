board = [(1, 20), (4, 100), (2, 50), (3, 160), (1, 30), (4, 60)]
for idx, value in enumerate(board):
    if value[1] == 160:
        print(board[idx-1][1])