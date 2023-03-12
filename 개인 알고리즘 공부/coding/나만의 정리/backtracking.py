import sys
sys.stdin = open('input','r')
# n과 m 부분집합구하기
def dfs(v,lst):
    if v == m:
        ans.append(lst)
        return
    for j in range(1, n+1):
        if visited[j] == 0:
            visited[j] = 1
            dfs(v + 1, lst + [j])
            visited[j] = 0

# 부분집합구하기 2
rs = []
def recur(num):
    if num == m:
        print(' '.join(map(str,rs)))
    for i in range(1,n+1):
        if visited[i]==0:
            visited[i]==1
            rs.append(i)
            recur(num+1)
            visited[i] = 0
            rs.pop()

n,m = list(map(int,input().split()))
ans = []
visited = [0]*(n+1)
dfs(0, [])
for a in ans:
    print(*a)
