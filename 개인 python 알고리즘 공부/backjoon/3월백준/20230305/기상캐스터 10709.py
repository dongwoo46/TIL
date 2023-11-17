import sys
sys.stdin = open('input', 'r')
n,m = list(map(int,input().split()))
weather = []
result = []
loc = 0
for i in range(n):
    ans = [-1]*m
    a = input()
    weather.append(a)
    for j in range(m):
        if a[j] == 'c':
            ans[j] = 0
            loc = j
        else:
            if 0 in ans:
                ans[j] =  abs(loc-j)
    result.append(ans)
for k in result:
    print(*k)




