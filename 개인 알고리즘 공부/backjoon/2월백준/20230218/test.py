def dfs(start, depth):
    # print(f'dp는', dp)
    if depth == 6:
        for j in range(6):
            print(dp[j], end=' ')
        print()
        return
    for i in range(start, len(arr)):
        # print(f'start는',start)
        # print(f'depth는', depth)
        # print(f'i는', i)
        # print(f'arr[i]는', arr[i])
        dp[depth] = arr[i]
        dfs(i + 1, depth + 1)

while True:
    dp = [0 for i in range(13)]
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]
    dfs(0, 0)
    print()