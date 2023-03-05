import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1,T+1):

    n,q = list(map(int,input().split()))
    box = [0]*(n+1)
    for i in range(1,q+1):
        l,r = list(map(int,input().split()))
        for j in range(l,r+1):
            box[j] = i

    print(f'#{tc}', *box[1:])

