def backtracking(v):
    if v == M:
        print(' '.join(map(str,result)))
    else:
        for i in range(1,N+1):
            if result:
                if result[-1] <= i:
                    result.append(i)
                    backtracking(v+1)
                    result.pop()
            else:
                result.append(i)
                backtracking(v+1)
                result.pop()

N,M = list(map(int,input().split()))
result = []
visited = [0]*(N+1)
backtracking(0)
