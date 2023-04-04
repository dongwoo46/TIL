import sys
sys.stdin = open('input','r')

# def find_set(x):
#     if parent[x] != x:
#         parent[x] = find_set(parent[x])
#     return parent[x]


def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    if x>y:
        parent[x] = y
    else:
        parent[y] = x

T = int(input())
for tc in range(1,T+1):
    v,e = map(int,input().split())
    parent = [x for x in range(v+1)]
    edges = []
    total = 0
    for _ in range(e):
        v1,v2,cost = map(int,input().split())
        edges.append((cost,v1,v2))
    edges.sort()
    for edge in edges:
        cost, v1, v2 = edge
        if find_set(v1) != find_set(v2):
            union(v1,v2)
            total += cost
    print(f'#{tc}',total)


