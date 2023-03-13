def backtracking(v,lst):
    if v == M:
        print(*lst)
        return
    else:
        last = 0
        for i in range(N):
            if not visited[i] and last != arr[i]:
                if lst:
                    if lst[-1]<= arr[i]:
                        visited[i] = 1
                        last = arr[i]
                        backtracking(v + 1, lst + [arr[i]])
                        visited[i] = 0
                else:
                    visited[i] = 1
                    last = arr[i]
                    backtracking(v + 1, lst + [arr[i]])
                    visited[i] = 0




N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
visited = [0]*N
backtracking(0,[])