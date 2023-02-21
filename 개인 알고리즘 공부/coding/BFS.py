v,e = map(int,input().split())# v는 정점 E는 엣지 갯수
arr = list(map(int,input().split()))
adjL = [[] for _ in range(v+1)]

for i in range(e):
    n1,n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    adjL[n2].append(n1)

def bfs(V, N):  #v 시작점 N 정점의 개수
    visited = [0]*(N+1) # visited 생성
    q = [V] # 큐 생성

    # 시작점 인큐
    visited[V] = 1 # 시작점 인큐표시
    while q: #큐가 비어있지 않으면
        t = q.pop(0) #디큐
        print(t, end = ' ') #t에서 처리할 일
        for i in adjL[t]: # t에 인접하고 방문한 적이업는 v
            if visited[i] == 0:
                q.append(i)# v인큐
                visited[i] = visited[t] + 1 # v 인큐되었음 표시
        print(visited)



bfs(1,v)
