if r<= l and c>=l:
    full(board,0,0,l)
    # print(board[])
elif r<=l and c<=l:
    for i in range(2):
        divide(0,0,l)
elif r>l and c<l:
    for i in range(3):
        divide(0,0,l)
else:
    for i in range(4):
        divide(0,0,l)