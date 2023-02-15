n, a, b = map(int, input().split())
tile_a = list(map(int, input().split()))
tile_b = list(map(int, input().split()))

tile_b.sort()
tile_a.sort()
dp = [0] * (n+1)
dp[1] = tile_a[0]
for i in range(2, n+1):
    dp[i] = dp[i-1] + tile_a[min(i-1, a-1)]
    if i >= 2:
        dp[i] = max(dp[i], dp[i-2] + tile_b[min((i-2)//2, b-1)])
print(dp[n])