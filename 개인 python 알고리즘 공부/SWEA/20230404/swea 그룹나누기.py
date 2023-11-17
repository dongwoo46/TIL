import sys
sys.stdin = open('input','r')

# x를 포함하는 집합을 찾는 연산 (대표원소 찾기)
def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])

# x,y를 포함하는 두 집합을 통합하는 연산
# 대표원소가 다른 집합의 대표원소를 가르키도록 변경
def union(x,y):
    x = find_set(x) # x가 속한 집합의 대표원소
    y = find_set(y) # y가 속한 집합의 대표원소
    if rank[x] >= rank[y]:
        parent[y] = x
    else:
        parent[x] = y
    if rank[x] == rank[y]:
        rank[x]+=1





T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    data = list(map(int,input().split()))
    parent = [i for i in range(n+1)]
    rank = [0] * (n+1)

    for i in range(m):
        union(data[2*i],data[2*i+1])

    groups = set() # 중복제거
    for j in range(1,n+1):
        # 대표 원소값들을 gropus에 집어넣고 중복제거하면  몇개의 그룹이 형성되는지 알 수 있다.
        groups.add(find_set(j))

    print(f'#{tc}', len(groups))
