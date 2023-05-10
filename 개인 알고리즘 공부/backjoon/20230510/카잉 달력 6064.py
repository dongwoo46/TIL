import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m,n,x,y = map(int,input().split())

    day = [1,1]
    cnt = 1
    while True:
        if day[0] == x and day[1] ==y:
            print(cnt)
            break
        if day[0] < m:
            day[0]+=1
        else:
            day[0] = 1
        if day[1] < n:
            day[1]+=1
        else:
            day[1] = 1
        if day[0] == 1 and day[1] == 1:
            print(-1)
            break
        cnt +=1
