import sys
sys.stdin = open('input', 'r')

def makeline(x):
    cnt = 0
    for line in arr:
        cnt+= line//x
    return cnt

def binarysearch(arr):
    start = 1 #최대 선
    end = max(arr) # 최소 선
    mx = 0
    while start<=end:
        mid = (start+end)//2

        if makeline(mid)<n:
            end=mid-1
        else:
            start= mid +1
    return end

k,n = map(int,input().split())
arr = [int(input()) for _ in range(k)]
result = []
print(binarysearch(arr))







