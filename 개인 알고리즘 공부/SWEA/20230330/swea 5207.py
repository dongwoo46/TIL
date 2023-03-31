# 이진탐색 해서 a[mid] == target이면 pass a[mid]>target 이라면 left+=1 else right+=1해서
# left != break 하고 break가 안일어나면 cnt+=1

import sys
sys.stdin = open('input')

def binarysearch(arr,target):
    global cnt
    # left = 0
    last = 0
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            cnt+=1
            return
        elif arr[mid] > target:
            end = mid-1
            # left+=1
            if last!=1:
                last = 1
            else:
                return
        else:
            start = mid+1
            if last!=2:
                last =2
            else:
                return
            # right+=1
        # if abs(right-left)>=2:
        #     return




T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    cnt = 0
    left = 0
    right = 0
    a.sort()
    for i in b:
        binarysearch(a,i)


    print(f'#{tc}',cnt)

