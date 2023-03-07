import sys
sys.stdin = open('input','r')
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
visited = [0]*n
check = [0]*n
a.sort()
ans = 0
idx = 0
a_idx = 0
while sum(visited) != n:
    mx = -1
    for i in range(n):
        if mx<b[i] and visited[i] == 0:
            mx = b[i]
            idx = i
    check[idx] = a[a_idx]
    visited[idx] = 1
    a_idx+=1

for i in range(n):
    ans += check[i] * b[i]

print(ans)
