T = int(input())
for tc in range(1,T+1):
    n = float(input())
    digit = 1
    ans = ''
    while digit !=13:
        if n == 0:
            break
        n = n*2
        ans += str(int(n))
        n -= int(n)
        digit +=1
    if n == 0:
        print(f'#{tc}',ans)
    else:
        print(f'#{tc}','overflow')


