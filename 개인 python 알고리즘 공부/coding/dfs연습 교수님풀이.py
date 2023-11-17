import sys
sys.stdin = open('input','r')
'''
1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7
'''
def dfs(node, visited):
    if node not in visited:
        visited.append(node)

        for w in graph[node]:
            if w not in visited:
                dfs(w,visited)

graph = {}

data = input().split(',')

for i in range(0,len(data),2):
    v1,v2 = data[i],data[i+1]
    if v1 in graph.keys(): # 이미 그래프의 key로 존재 했다면
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]
    if v2 in graph.keys(): # 이미 그래프의 key로 존재 했다면
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]

visited = []
dfs(1,visited)
for i in visited:
    print(i, end=' ')
print()

# dfs 탐색시 연결 노드 큰값부터 먼저 방문하는 코드
visited = []
graph = {k: sorted(v,reverse=True) for k,v in graph.items()}
dfs(1,visited)
for i in visited:
    print(i, end=' ')
print()