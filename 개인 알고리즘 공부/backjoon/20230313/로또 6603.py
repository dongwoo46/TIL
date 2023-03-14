import sys
sys.stdin = open('input','r')

def backtracking(v):
    if v == 6:
        print(*result)
    else:
        for i in range(1,k+1):
            if not visited[i]:
                if result:
                    if result[-1] < arr[i]:
                        visited[i] = 1
                        result.append(arr[i])
                        backtracking(v+1)
                        visited[i] = 0
                        result.pop()
                else:
                    visited[i] = 1
                    result.append(arr[i])
                    backtracking(v + 1)
                    visited[i] = 0
                    result.pop()

while True:
    arr = list(map(int,input().split()))
    k = arr[0]
    s = arr[1:]
    visited = [0]*(k+1)
    result = []
    if k> len(s) or k == 0:
        break
    backtracking(0)
    print()
