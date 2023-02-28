n = int(input())
numb_list = [x for x in range(1,(n//2)+2)]

cnt = 0

for i in range(1, n+1):
    x=i
    all = 0
    while True:
        if all == n:
            cnt += 1
            break
        elif all >n:
            break
        else:
            all += x
            x += 1

print(cnt)