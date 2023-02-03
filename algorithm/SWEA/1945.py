T = int(input())


for tc in range(1, T+1):
    a = b = c = d = e = 0
    n = int(input())
    while n != 1:
        if n%11 == 0:
            n= n//11
            e+=1
        elif n%7 == 0:
            n = n//7
            d+=1
        elif n%5 == 0:
            n = n//5
            c+=1
        elif n%3 == 0:
            n = n//3
            b+=1
        else:
            n = n//2
            a +=1
    print(f'#{tc} {a} {b} {c} {d} {e}')
