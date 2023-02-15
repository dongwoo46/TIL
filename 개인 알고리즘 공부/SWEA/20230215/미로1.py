import sys

sys.stdin = open('input', 'r')
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 내가 간곳 저장

def move(maze):
    # 상하좌우 4방향 확인해서 인덱스 범위 안넘고 미로값이  0이면
    # if not stack:
    #     print(maze)
    # else:
    #     print(stack[-1])
    #     print(stack)
    if stack:
        #상하좌우 4가지 방향 체크
        for direction in range(4):
            x = stack[-1][0]
            y = stack[-1][1]
            x += dx[direction]
            y += dy[direction]
            #만약 x,y의 인덱스가 벗어나지 않고
            if 0 <= x < n and 0 <= y < n:
                #만약 maze의 좌표가 3이면
                if maze[x][y] == '3':
                    visited[x][y] = 1
                    return 1
                #만약 mazey가 0 이거나 visited가 1이 아니면 stack에 집어넣고 재귀
                elif maze[x][y] == '0' and visited[x][y] != 1:
                    stack.append((x, y))
                    visited[x][y] = 1
                    return move(maze)
        # 위에 4방향을 다 체크했는데 만약 스택이 남아잇으면 스택을 pop하고 재귀

        else:
            if stack:
                stack.pop()
                return move(maze)
            #스택이 안남아있으면 0리턴

            else:
                return 0
    #스택이 처음부터 없으면 0
    if not stack:
        return 0



T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    stack = []
    maze = []
    visited = [[0] * (n) for _ in range(n)]
    for _ in range(n):
        maze.append(input())

    # 2출발 1벽 3도착
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '1':
                visited[i][j] = 1
            elif maze[i][j] == '2':
                visited[i][j] = 1
                stack.append((i, j))
    if not stack:
        print(f'#{tc}',0)
    else:
        print(f'#{tc}',move(maze))
