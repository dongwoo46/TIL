'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

def dijkstra(s,v): # s 출발, v 마지막 정점 번호
    U = [0]*(v+1) # U 최소비용이 결정된 정점 집합
    U[s] = 1 # U = {s}
    for i in range(v+1): # s에서 나머지 정점 i 로 가는 비용
        D[i] = adjM[s][i]

    # while U!=V: 남은 정점의 비용 결정
    n = v+1 # n개의 정점
    for _ in range(n-1): # n-1개 정점의 비용 결정
        # D[w]가 최소인 w결정
        minV = INF
        w = 0
        for i in range(v+1):
            if U[i] ==0 and minV>D[i]: # 남은 정점 i중 최소
                w = i
                minV= D[i]
    U[w] = 1 # 최소인 w는 최소 비용 D[w] 확정
    # w에 인접인 정점에 대해, 기존비용 vs w 를 거처가는 비용 비교
    for v in range(v+1):
        if 0<adjM[w][v]<INF: # w에 인접인 v의 조건
            D[v] = min(D[v],D[w]+adjM[w][v])

INF = 1e9 # 문제에 따라

v,e = map(int,input().split()) # 0~v번 정점, e간선 수
adjM = [[INF]*(v+1) for _ in range(v+1)]
for i in range(v+1):
    adjM[i][i] = 0
for _ in range(e):
    u,v,w = map(int,input().split()) # u->v,w 가중치
    adjM[u][v] = w

D = [0]*(v+1)
