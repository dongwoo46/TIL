import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    v,e = list(map(int,input().split()))

    visited = [False]*(v+1)
    graph = [[] for _ in range(v+1)]
    res = []
    for _ in range(e):
        a,b = list(map(int,input().split()))
        graph[a].append(b)

    start, end = list(map(int,input().split()))

    def dfs(graph, v, visited):
        visited[v] = True
        res.append(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    dfs(graph, start, visited)
    if end in res:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)





