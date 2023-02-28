import sys
sys.stdin = open('input', 'r')

def selectionsort(arr, N):
    for i in range(N-1): #작업 구간의 시작 인덱스
        minidx = i # 맨 앞이 최소라 가정
        for j in range(i+1,N): #i보다 큰 나머지 구간에서 탐색
            if arr[minidx] > arr[j]: #만약 minidx가 가르키는 애보다 j의 값이 작다면 j가 minidx가 된다
                minidx = j
        #arr[i]와 arr[minidx]의 위치를 서로 바꿔준다!
        arr[i], arr[minidx] = arr[minidx], arr[i]
    return arr

n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

stack.sort()
for i in stack:
    print(i)


