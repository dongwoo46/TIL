# 백준 1074 Z
import sys
sys.stdin = open('input','r')


def divide(x,y,n):
    global cnt
    if x>r or x+n<=r or c<y or y+n<=c:
        cnt += n**2
        return
    if n==2:
        full(x,y,n)
    else:
        divide(x,y,n//2)
        divide(x,y+n//2,n//2)
        divide(x+n//2,y,n//2)
        divide(x+n//2,y+n//2,n//2)
        return


def full(x,y,n):
    global cnt
    global ans
    if x==r and y==c:
        ans = cnt
    elif x==r and y+1==c:
        ans = cnt+1
    elif x+1==r and y==c:
        ans = cnt+2
    else:
        ans = cnt+3
    return

N, r, c = map(int,input().split())

ans = 0
cnt = 0
divide(0,0,2**N)
print(ans)
