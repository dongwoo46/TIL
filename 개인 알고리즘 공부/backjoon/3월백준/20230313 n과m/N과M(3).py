def backtracking(v):
    if v == M:
        print(' '.join(map(str,result)))
        return
    else:
        for i in range(1,N+1):

            result.append(i)
            backtracking(v+1)
            result.pop()



N,M = list(map(int,input().split()))
visited = [0]*(N+1)
result = []
backtracking(0)