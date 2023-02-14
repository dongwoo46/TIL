import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1,T+1):
    #k 노드 수 #e 그래프 입력횟수
    k,e = list(map(int,input().split()))

    visited = [False]*(k+1)
    graph = [[]*(k+1) for _ in range(k+1)]
    res = []
    stack = []

    for _ in range(e):
        a,b = list(map(int,input().split()))
        graph[a].append(b)

    # for _ in range(e):
    #     a,b = map(int,input().split())
    #     graph[a][b] = 1


    start, end = list(map(int, input().split()))
    v = start
    visited[v] = True
    res.append(v)

    while True:
        found = False
        #v에서 출발하고 도착하는 점이 w가 1이고 visied가 False이면
        for w in graph[v]:
            if visited[w] == False:
                stack.append(v)
                v = w
                visited[w] = True #w에 방문함
                res.append(w)
                found = True
                break

        if not found: # found가 false이면
            if stack:
                v = stack.pop()
            else: #스택이 비어있으면
                break

    if end in res:
        print(f'#{tc}', 1)
    else:
        print(f'#{tc}', 0)

