import sys
sys.stdin = open('input','r')
import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[0] = 0
    while q:
        min_dist, now = heapq.heappop(q)
        if distance[now] < min_dist:
            continue
        for i in graph[now]:
            cost = min_dist + i[1]
            if cost<distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    distance = [int(1e9)]*(v+1)
    for _ in range(e):
        v1,v2,c = map(int,input().split())
        graph[v1].append((v2,c))

    dijkstra(0)
    print(f'#{tc}', distance[v])

