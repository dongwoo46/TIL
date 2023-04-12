a = 0
k = 0

def top(board, v):
    global a,k
    for i in range(5):
        if board[i][v]:
            a = board[i][v]
            k = i
            break
    else:
        a = 0

    return

def solution(board, moves):
    global a,k
    answer = 0
    stack = []
    for i in moves:
        top(board, i - 1)
        if stack:
            if stack[-1] ==a:
                answer += 2
                board[k][i-1]=0
                stack.pop()
            else:
                if a !=0:
                    stack.append(a)
                    board[k][i-1] = 0
                else:
                    continue
        else:
            if a !=0:
                stack.append(a)
                board[k][i-1] = 0
            else:
                continue

    return answer
board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves =[1,5,3,5,1,2,1,4]
print(solution(board,moves))
