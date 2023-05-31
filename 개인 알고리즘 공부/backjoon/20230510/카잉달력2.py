import sys
sys.stdin = open('input','r')
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m,n,x,y = map(int,input().split())
    temp = x
    while temp<=m*n:
        if temp%n == y%n:
            print(temp)
            break
        temp +=m
    else:
        print(-1)