import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int,input().split()))
    uclid =  abs(x1-x2)**2+abs(y1-y2)**2
    distance = uclid**0.5
    if distance == 0 and r1 == r2:
        print(-1)
    elif distance == r1 + r2:
        print(1)
    elif abs(r1-r2)<distance<r1+r2:
        print(2)
    elif abs(r1-r2) == distance:
        print(1)
    else:
        print(0)
