import sys
input = sys.stdin.readline
INF = int(1e9) #무한 값 10억

# 노드의 개수, 간선의 개수 입력받기
n,m = map(int,input().split())
#시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결된 노드에 대한 정보담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적 리스트 만들기
visited = [False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance= [INF]*(n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int,input().split())
    # a번 노드에서 b번노드로 가는 비용이 c라는 뜻
    graph[a].append((b,c))

# 방문 하지 않은 노드중에서 거리가 가장짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        # 최소 거리이고 방문하지 않은 노드라면
        if distance[i] < min_value and not visited[i]:
            # 최소값은 해당 노드의 distance값
            min_value = distance[i]
            # 해당 노드의 번호가 인덱스
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    # 방문 체크
    visited[start] = True
    # start와 연결된 노드들 거리값 집어넣기
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    for j in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            # 비용은 현재노드에서 다른노드로 가는 값과 현재까지 오는데 사용된 값 더해주기
            cost = distance[now]+j[1]
            # 해당 노드의 현재 distance값보다 해당 노드로 이동해서 오는 거리가 짧을 때 해당 노드의 distance값 변경
            if cost<distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 실행
dijkstra(start)

# 모든 노드로 가기위한 최단 거리를 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])




