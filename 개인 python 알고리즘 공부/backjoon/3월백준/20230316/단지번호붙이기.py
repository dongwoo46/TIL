import sys

sys.stdin = open('input', 'r')

def bfs(x,y):
    q = [(x,y)]
    visited[x][y] = total
    cnt = 1
    while q:
        x,y = q.pop(0)
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0 and board[nx][ny]==1:
                visited[nx][ny]= total
                q.append((nx,ny))
                cnt +=1
    return cnt


total = 1
n = int(input())
board = [list(map(int,input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
result = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 1 and visited[x][y] == 0:
            result.append(bfs(x,y))
            total+=1

print(total-1)
result.sort()
for i in result:
    print(i)



