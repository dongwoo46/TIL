import sys
sys.stdin = open('input','r')

# 자기보다 1크거나 자기자신과 index가 같은 것만 고를 수 있음
n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i][j]+dp[i-1][j]
        elif j == i:
            dp[i][j] = dp[i][j] +dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))