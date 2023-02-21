import sys
sys.stdin = open('input','r')

def bfs(v):
    visited = [0]*(101)
    q = [v]
    visited[v] = 1
    global res
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1
    for i in range(100,-1,-1):
        if visited[i] == max(visited):
            res = i
            return res


def chunk(list1,n):
    return [list1[i:i+n] for i in range(0,len(list1), n)]

for tc in range(1,11):
    n,start = list(map(int,input().split()))

    e = list(map(int,input().split()))
    graph = [[] for _ in range(101)]
    res = 0
    for i in range(n//2):
        a, b = e[i*2], e[i*2+1]
        graph[a].append(b)

    print(f'#{tc}' , bfs(start))
