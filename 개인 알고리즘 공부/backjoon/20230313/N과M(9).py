import sys
import time
sys.stdin = open('input','r')
start = time.time()

def backtracking(v):
    if v == M:
        print(' '.join(map(str,result)))
    else:
        last = -1
        for i in range(N):
            if not visited[i] and last != arr[i]:
                visited[i] = 1
                last = arr[i]
                result.append(arr[i])
                backtracking(v+1)
                visited[i] = 0
                result.pop()

N,M = map(int,input().split())
arr = sorted(list(map(int,sys.stdin.readline().split())))
result = []
visited = [0]*N
backtracking(0)



end = time.time()
print('time : ', end-start)