def backtracking(v):
    if v == M:
        print(' '.join(map(str,result)))
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                result.append(arr[i])
                backtracking(v+1)
                visited[i] = 0
                result.pop()








N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0]*(N+1)
result = []
backtracking(0)