import sys
sys.stdin = open('input','r')

#v출발 . n은 노드수
def bfs(graph,v,n):
    visited = [0]*(n+1)
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        # print(t, end = '')
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t]+1
    return visited

T = int(input())
for tc in range(1,T+1):
    v,e = list(map(int,input().split()))
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a,b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)
    depart, arrive = list(map(int,input().split()))

    if bfs(graph, depart, v)[arrive] == 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', bfs(graph, depart, v)[arrive] - 1)

