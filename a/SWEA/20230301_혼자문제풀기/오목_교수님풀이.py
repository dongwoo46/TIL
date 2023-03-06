import sys
sys.stdin = open('input','r')

#상하좌우 대각선방향을 모두 볼 필요 없으므로 겹치는 방향중 한가지 방향 4가지만 확인
delta = [(1,0),(0,1),(1,1),(1,-1)]
#범위 체크
def is_valid(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False

#o가 5개인지 확인하는 함수
def count5():
    for x in range(n):
        for y in range(n):
            #board가 o일때 델타를 이용하여 한 방향당 5번 확인
            if board[x][y] == 'o':
                for dx,dy in delta:
                    for i in range(5):
                        nx = x + dx*i
                        ny = y + dy*i
                        # 만약 범위를 벗어 나거나 . 이면 반복 종료
                        if not is_valid(nx,ny) or board[nx][ny] == '.':
                            break
                    #반복이 끊기지 않고 5번다 돌면 yes 리턴
                    else:
                        return 'YES'
    #만약 못찾으면 no return
    return 'NO'

T = int(input())

for tc in range(1,T+1):
    n = int(input())

    board = [list(input()) for _ in range(n)]

    print(f'#{tc} {count5()}')
