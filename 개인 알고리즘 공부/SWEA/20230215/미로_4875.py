import sys
sys.stdin = open('input','r')
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0

 # 내가 간곳 저장

def move(maze):
    while True:
        global result
        if result == -1:
            break
        if stack:
            x = stack[-1][0]
            y = stack[-1][1]
            # 상하좌우 4방향 확인해서 인덱스 범위 안넘고 미로값이  0이면
            for direction in range(4):
                x += dx[direction]
                y += dy[direction]
                if 0<=x<n and 0<=y<n and maze[x][y] == '0' and visited[x][y] !=1:
                    stack.append((x,y))
                    visited[x][y] = 1
                    if maze[x][y] == '3':
                        return 1

                    else:
                        return move(maze)
                else:
                    if stack:
                        stack.pop()
                        return move(maze)
                    else:

                        return -1
                        break

        elif not stack:
            return -1
            break


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    stack = []
    maze = []
    visited = [[0] *(n+1) for _ in range(n+1)]
    for _ in range(n):
        maze.append(input())

    # 2출발 1벽 3도착
    for i in range(n):
        for j in range(n):
            if maze[i][j] == '1':
                visited[i][j] = 1
            elif maze[i][j] == '2':
                visited[i][j] = 1
                stack.append((i,j))
                start_location = (i,j)
            else:
                continue

    print(move(maze))

#             check.append((x,y))
#             can_go.append((x,y))
#     if not check:
#         return -1
#     else:
#         return can_go
#
# def go_route(maze):
#     if find_route(maze) == -1:
#         if stack[-1]
#             stack.append(can_go.pop())
#
#         else:
#             stack.pop()
#     if length == len(can_go):
#         stack.pop()
#     else:
#         for go in can_go[::-1]:
#             if visited[go[0]][go[1]] == 0:
#                 stack.append((go[0],go[1]))
#                 can_go.pop()
#                 visited[go[0]][go[1]] = 1













