# SWEA 최소비용
import heapq
import sys
sys.stdin = open('input','r')

def dijkstra(x,y):
    q = []
    heapq.heappush(q, (0, x, y))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        if x == n-1 and y == n-1:
            return
        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]>board[x][y]:
                    need = abs(board[x][y] - board[nx][ny])
                else:
                    need = 0
                if distance[nx][ny]> distance[x][y]+need+1:
                    distance[nx][ny] = distance[x][y]+need+1
                    heapq.heappush(q,(distance[nx][ny],nx,ny))


INF = int(1e9)
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _  in range(n)]
    distance = [[INF]*n for _ in range(n)]
    dijkstra(0,0)
    print(f'#{tc}', distance[n-1][n-1])


'''
def dfs(v,x,y):
    global total,mn
    if total>=mn:
        return
    if v == 2*(n-1):
        mn = min(total,mn)
    for dx,dy in [(1,0),(0,1)]:
        nx = x + dx
        ny = y + dy
        if 0<=nx<n and 0<=ny<n:
            total += abs(board[x][y] - board[nx][ny])
            dfs(v+1,nx,ny)
            total -= abs(board[x][y]- board[nx][ny])
'''
'''
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    mn = 1e9
    v = 0
    total = 2*(n-1)
    dfs(0,0,0)
    print(f'#{tc}', mn)
'''




