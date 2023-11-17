import sys

sys.stdin = open('input', 'r')



# 내가 간곳 저장

def move(x,y):
    # 상하좌우 4방향 확인해서 인덱스 범위 안넘고 미로값이  0이면
    #상하좌우 4가지 방향 체크
    for direction in range(4):
        x += dx[direction]
        y += dy[direction]
        #만약 x,y의 인덱스가 벗어나지 않고
        if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
            #만약 maze의 좌표가 3이면
            if not maze[x][y]:
                visited[x][y] = 1
                if move(x,y):
                    return 1
            elif maze[x][y] == 3:
                return 1
            #만약 mazey가 0 이거나 visited가 1이 아니면 stack에 집어넣고 재귀

    # 위에 4방향을 다 체크했는데 만약 스택이 남아잇으면 스택을 pop하고 재귀

    # 2출발 1벽 3도착
def find_start(n,maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return 1 if move(i,j) else 0

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    maze = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print(f'#{tc}', int(find_start(n, maze)))




\

