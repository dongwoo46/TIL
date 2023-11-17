'''
<크루스칼 이용 MST>
1. 모든 간선을 가중치에 따라 오름차순 정렬
2. 가중치가 가장 낮은 간선부터 선택하면서 트리 증가 - 단 사이클 존재하면 다음으로 가중치가 낮은 간선 선택
- 각 정점들에 대한 유니온파인드 만들어야함. 각각 간선을 선택해서 유니온하고 간선의 대표정점이 같으면 사이클이 형성된것 이때 제외!!
3. n-1개의 간선이 선택될때까지 2)반복
'''

# find_set
def  find_set(x): # x가 속한 집합의 대표
    while x!=rep[x]: # x==rep[x]가 될때 까지
        x = rep[x]
    return x

# union(x,y)
def union(x,y): # y의 대표원소가 x의 대표원소를 가르키도록 함
    rep[find_set(y)] = find_set(x)
    # rep[y] = find_set(x) 하면 틀림!!!

v,e = map(int,input().split()) # 0~V 정점 번호, e 간선 수
# make_set()
rep = [x for x in range(6)]
graph = []
for _ in range(e):
    v1,v2, w = map(int,input().split())
    graph.append([v1,v2,w])
    # graph.append([w,v1,v2])
    # graph.sort()

# (1) 가중치 기준 오름차순 정렬
graph.sort(key=lambda x:x[2])

# (2)  N개의 정점(V+!), n-1개의 간선 선택
n = v+1
s = 0 #mst에 포함된 간선의 가중치 합
cnt = 0
MST = []
for u,v,w in graph: # 가중치가 작은 거부터
    if find_set((u)) != find_set(v): # 사이클이 생기지 않은면(대표값이 다르면)
        cnt+=1
        s+=w # 가중치 합
        MST.append((u,v,w))
        union(u,v)
        if cnt==n-1: # MST구성 완료
            break
print(s)