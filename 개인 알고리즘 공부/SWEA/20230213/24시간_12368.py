import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1,T+1):
    a, b = list(map(int,input().split()))
    ans = 0
    if a+b ==24:
        ans = 0
    elif a+b<24:
        ans = a + b
    else:
        ans = a + b -24
    print(f'#{tc} {ans}')


