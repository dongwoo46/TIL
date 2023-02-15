import sys
sys.stdin = open('input','r')

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

for tc in range(1,11):
    tc, long = list(map(int, input().split()))
    path = list(map(int, input().split()))
    path = list_chunk(path, 2)
    visited = [False] * 100
    graph = [[] for _ in range(100)]
    res = []
    for i in range(long):
        graph[path[i][0]].append(path[i][1])



    def dfs(graph, v, visited):
        visited[v] = True
        res.append(v)
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    dfs(graph,0,visited)

    if 99 in res:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}' ,0)





