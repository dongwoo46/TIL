# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
#
# 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.
import sys
sys.setrecursionlimit(10**5)
def dfs(r):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    global cnt
    visited[r] = cnt  # 시작 정점 R을 방문 했다고 표시한다. 왜 cnt를 쓰냐면 방문 순서를 차례로 뽑아야하기때문에
                        # r노드의 visited위치에 방문순서를 입력받아서 출력해서 순서대로 해댱 노드들의 방문순서 출력한다.

    for i in graph[r]:   # E(R) : 정점 R의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다)
        if not visited[i]:
            cnt+=1
            dfs(i)


n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 1

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in graph:
    x.sort()

dfs(r)

for i in range(1,n+1):
    print(visited[i])




# 5 5 1
# 1 4
# 1 2
# 2 3
# 2 4
# 3 4