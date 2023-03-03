import sys
sys.stdin = open('input','r')

T =int(input())
for tc in range(1,T+1):
    n,m = list(map(int,input().split()))
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    max_mult = 0

    if len(a)> len(b):
        long = a
        short = b
    else:
        long = b
        short = a
    for i in range(len(long)-len(short)+1):
        mult = 0
        k = 0
        for j in range(i,i+len(short)):
            mult += long[j]*short[k%len(short)]
            k+=1
        max_mult = max(mult,max_mult)

    print(f'#{tc}',max_mult)

