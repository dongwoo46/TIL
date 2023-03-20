import sys
sys.stdin = open('input', 'r')


def tree_length(x):
    total = 0
    for i in tree:
        if i - x > 0:
            total += i-x
    return total


def binarysearch(arr):
    start = 1 # 가져갈나무 최대
    end = max(tree) #가져갈나무 최소
    while start <= end:
        mid = (start+end)//2
        if tree_length(mid) == m:
            return mid
        elif tree_length(mid) > m:
            start = mid + 1
        else:
            end=mid- 1
    return start

n,m= map(int,input().split())
tree = list(map(int,sys.stdin.readline().split()))
h = 0
print(binarysearch(tree))




#시간 복잡도 n = 100만