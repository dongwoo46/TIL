# t(n) = t(n-1)+t(n-2)
import sys
sys.stdin= open('input', 'r')
n = int(input())
stair = [int(input()) for _ in range(n)]
numb = [0]*n

if n == 1:
    print(stair[0])
elif n == 2:
    print(stair[0]+stair[1])
else:
    numb[0] = stair[0]
    numb[1] = stair[1]+stair[0]
    numb[2] = max(stair[0]+stair[2],stair[1]+stair[2])
    for i in range(2,n):
        numb[i] = max(numb[i-2]+stair[i],numb[i-3]+stair[i-1]+stair[i])
    print(numb[n-1])