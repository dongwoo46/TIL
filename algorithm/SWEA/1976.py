T = int(input())


for t in range(1,T+1):
    a, b, c, d = list(map(int,input().split()))
    hour = a+c
    mnt = b+d
    
    if b+d >= 60:
        if a+c+1>12 and a+c+1<24:
            hour = a+c+1-12
            mnt = b+d-60
        elif a+c+1>=24:
            hour = a+c+1-12
            mnt = b+d-60
        elif a+c+1<=12:
            hour = a+c+1
            mnt = b+d-60
            
    else:
        if a+c>12 and a+c<24:
            hour = a+c-12
            mnt = b+d
        elif a+c<=12:
            hour = a+c
            mnt = b+d
        elif a+c>24:
            hour = a+c-12
            mnt = b+d
    print(f'#{t} {hour} {mnt}')