# hoare

def hoare(A,l,r):
    pivot = A[l]
    i = l
    j = r
    while i<=j:
        while i<=j and A[i]<=pivot:
            i += 1
        while i<=j and A[i]>=pivot:
            j-=1
        if i<j:
            A[i],A[j] = A[j],A[i]
    A[j],A[l] = A[l],A[j]
    return j

def qsort(A,l,r):
    if l<r:
        s = hoare(A,l,r)
        qsort(A,l,s-1)
        qsort(A,s+1, r)

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    qsort(arr,0,N-1)
    print(*arr,cnt)