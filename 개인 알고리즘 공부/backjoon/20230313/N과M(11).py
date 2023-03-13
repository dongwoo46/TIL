import sys
sys.stdin = open('input','r')
def backtracking(v):
    if v == M:
        print(*result)
        return

    for i in range(N):
        if arr[i] == arr[i+1]:
            continue
        else:
            if result:
                if arr[i] != arr[i+1]:
                    result.append(arr[i])
                    backtracking(v+1)
                    result.pop()
            else:
                result.append(arr[i])
                backtracking(v+1)
                result.pop()





N, M = map(int,input().split())
arr = sorted(list(map(int,input().split())))+[' ']
result = []
backtracking(0)

