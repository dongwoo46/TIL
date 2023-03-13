def backtracking(v):
    if v == M:
        print(' '.join(map(str,result)))
    else:
        for i in range(N):
            result.append(arr[i])
            backtracking(v+1)
            result.pop()



N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = []
visited = [0]*N
backtracking(0)