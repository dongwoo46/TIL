import sys
sys.stdin = open('input', 'r')

def bfs(v, n): #v 시작노드 n 노드 수
    visited = [0] *(n+1)
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        print(t, end=' ')
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1


def dfs(v,n): #v 시작노드 n 노드수
    visited[v] = 1
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i,n)

# def bfs(x,y,cnt):
#     q = [(x,y,cnt)]
#     while q:
#         x,y,cnt = q.pop(0)
#         for dx,dy in delta:
#             nx = x + dx
#             ny = y + dy
#             if 0<=nx<n and 0<=ny<m:
#                 if maze[nx][ny] == 1:
#                     maze[nx][ny] = 0
#                     q.append((nx,ny,cnt+1))
#                 elif x == n-1 and y == m-1:
#                     return cnt


v,e,start = list(map(int,input().split()))
graph = [[] for _ in range(v+1)]
visited = [0] * (v + 1)
for i in range(e):
    n1,n2 = list(map(int,input().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)

for x in graph:
    x.sort()


dfs(start,v)
print()
bfs(start,v)


