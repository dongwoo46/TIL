import sys
sys.stdin = open('input','r')

n = int(input())
wine = [0]*10001
for i in range(n):
    wine[i] = int(input())
dp = [0]*10001

# result를 각 번호에 왔을 때 마실 수 있는 최대 양이라고 하자
# 첫번째 마셨을 때는 wine[0] 가 최대 값
# 두번째 마셨을 때는 wine[0]+wine[1] 이 최대값
# 세번째 마셨을 때는 wine[0]+wine[2] or wine[0]+wine[1] or wine[1]+wine[2]
# 즉 3가지 경우가 존재
# 1. 자신의 번호를 마시고 자신의 이전 번호 까지 마신다면 -> 이전번호의 이전은 버리고 그 이전칸의 최대 값까지 더해줌
# 2. 자신의 번호를 마시고 이전번호는 안마시면 -> 자신의 번호+이전이전의 번호 최대값
# 3. 자신의 번호 안마시면 -> 자신 이전 번호 최대값
dp[0] = wine[0]
dp[1] = wine[0]+wine[1]
for i in range(2,n+1):
    dp[i] = max(wine[i]+wine[i-1]+dp[i-3],wine[i]+dp[i-2],dp[i-1])

print(max(dp))
