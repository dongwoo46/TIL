
t = int(input())



def maxm(numbs):
    maxV = numbs[0]
    for number in numbs:
        if maxV<=number:
            maxV = number
    return maxV

for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        count = 0
        for j in range(i,n):
            if arr[i] > arr[j]:
                count += 1
        arr[i] = count

    print(f'#{tc} {max(arr)}')

