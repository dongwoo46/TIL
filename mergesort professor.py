import sys
sys.stdin= open('input')

# 병합정렬 교수님

def msort(s,e):
    if s==e:
        return
    m = (s+e)//2
    msort(s,m)
    msort(m+1,e)
    k = 0
    l, r = s, m+1 # 왼쪽파트와 오른쪽파트에서 가장 작은 숫자의 위치
    while l<=m or r <=e :
        if l<=m and r<=e: # 둘다 left,right의 범위 안에 있음
            if arr[l]<=arr[r]:
                temp[k] = arr[l]
                l +=1
            else:
                temp[k] = arr[r]
                r +=1
            k +=1
        elif 1<=m: # 만약 한 쪽의 복사(정렬)이 끝났는데 한쪽이 남아있으면
            while l<=m:
                temp[k] = arr[l]
                l+=1
                k+=1
        elif r<=e:
            while r<=e:
                temp[k] = arr[r]
                r += 1
                k += 1
    i = 0
    while i<k:
        arr[s+i] = temp[i]
        i+=1
    return arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0]*N
    print(msort(0,N-1))
