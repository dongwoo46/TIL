import sys
sys.stdin = open('input','r')

def bfs(v):
    global cnt
    q = [v]
    visited[v] =1
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
    cnt+=1

T= int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    visited[0] = 1
    cnt = 0
    for i in range(m):
        a,b = arr[i*2], arr[i*2+1]
        graph[a].append(b)
        graph[b].append(a)
    for i in range(n+1):
        if not visited[i]:
            bfs(i)
    print(f'#{tc}', cnt)
