import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    cnt = 0
    f = [0]*12
    f[1] = 1
    f[2] = 2
    f[3] = 4
    for i in range(4,n+1):
        f[i] = f[i-1]+f[i-2]+f[i-3]
    print(f[n])