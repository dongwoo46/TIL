import sys
import heapq
sys.stdin = open('input','r')

v,e = map(int,input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [1e9]*(v+1)

for _ in range(e):
    u,a,w = map(int,input().split())
    graph[u] .append((a,w)) # graph안에는 (노드,가중치(거리))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # heapq 에도 (노드, 가중치(거리))
    distance[start] = 0
    while q:
        min_dist, now  = heapq.heappop(q)
        if distance[now] < min_dist:
            continue
        for i in graph[now]:
            cost = i[1] + min_dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == 1e9:
        print('INF')
    else:
        print(distance[i])

