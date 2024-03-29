import sys
input = sys.stdin.readine
INF = int(1e9)

def bf(start):
    # 시작노드에 대해 초기화
    dist[start] = 0
    # 전체 n번의 라운드 반복
    for i in range(n):
        cur = edges[j][0]
        next_node = edges[j][1]
        cost = edges[j][2]
        # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if dist[cur] != INf and dist[next_code] > dist[cur] + cost:
            dist[next_node] = dist[cur] + cost
            # n번째 라운드에서도 값이 갱신된다면 음수순환 존재
            if i == n-1:
                return True
    return False
# 노드수와 간선 수 입력받기
n,m = map(int,input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges=[]
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a,b,c))

# 벨만 포드 알고리즘 수행
negative_cycle = bf(1) # 1번 노드가 시작 노드

if negative_cycle:
    print("-1")
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])