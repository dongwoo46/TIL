def binarysearch(arr, N, key):
    start = 0
    end = N-1
    while start<=end:
        mid = (start + end)//2
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid]<key:
            start = mid + 1
        else:
            return card[start:end+1].count(key)
    return 0

import sys

n = int(input())
card = (list(map(int, sys.stdin.readline().split())))
m = int(input())
find = list(map(int, sys.stdin.readline().split()))

ans = {}
for i in card:
    if i in ans:
        ans[i] +=1
    else:
        ans[i] = 1

for j in find:
    if j in ans:
        print(ans[j], end=' ')
    else:
        print(0, end=' ')

