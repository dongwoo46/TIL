def backtracking(v):
    if v == M:
        print(' '.join(map(str,result)))
    else:
        for i in range(N):
            if result:
                if result[-1] <= arr[i]:
                    result.append(arr[i])
                    backtracking(v+1)
                    result.pop()
            else:
                result.append(arr[i])
                backtracking(v + 1)
                result.pop()


N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = []
backtracking(0)