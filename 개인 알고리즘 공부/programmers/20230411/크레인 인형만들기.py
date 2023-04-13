a = 0
k = 0

def top(board, v): # 보드에서 해당 열에서 가장 위에 있는거 뽑기
    global a,k
    for i in range(5):
        if board[i][v]:
            a = board[i][v]
            k = i
            break
    else: # for문을 다 돌때까지 a가 갱신 안되면 해당 열은 비어있다는 것 따라서 a = 0으로 바꿔줌
        a = 0

    return

def solution(board, moves):
    global a,k # a 캐릭터의 번호 k 캐릭터를 뽑앗을 때 행번호
    answer = 0
    stack = []
    for i in moves:
        top(board, i - 1) # 매번 moves에 대해 해당 열에 있는 가장 높은 캐릭터 뽑기
        if stack:  # 스택이 존재한다면
            if stack[-1] ==a: # stack의 마지막 값이 만약 현재 열의 가장 높은 캐릭터와 같다면
                answer += 2 # 스티커 2개가 지워지므로 answer+2
                board[k][i-1]=0 # 보드에서 해당 스티커 사용했으므로 0으로 바꿔줌
                stack.pop() # 스티커 지웠으므로 stack에서 마지막값 삭제
            else:
                if a !=0: # top이 비어잇지 않다면
                    stack.append(a) # stack에 a를 넣어주고
                    board[k][i-1] = 0 # 보드에 a가 들어있는 값을 0 으로 바꿔줌
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
