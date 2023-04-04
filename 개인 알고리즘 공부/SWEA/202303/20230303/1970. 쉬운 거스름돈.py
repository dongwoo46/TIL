import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    money_cnt = []
    cnt = 0
    while n>=50000:
        cnt +=1
        n -= 50000
    money_cnt.append(cnt)
    cnt = 0
    while n>=10000:
        cnt +=1
        n -= 10000
    money_cnt.append(cnt)
    cnt = 0
    while n>=5000:
        cnt+=1
        n -= 5000
    money_cnt.append(cnt)
    cnt = 0
    while n>=1000:
        cnt+=1
        n-=1000
    money_cnt.append(cnt)
    cnt = 0
    while n>=500:
        cnt +=1
        n-=500
    money_cnt.append(cnt)
    cnt = 0
    while n >= 100:
        cnt += 1
        n -= 100
    money_cnt.append(cnt)
    cnt = 0
    while n>=50:
        cnt +=1
        n-=50
    money_cnt.append(cnt)
    cnt = 0
    while n>=10:
        cnt +=1
        n-=10
    money_cnt.append(cnt)

    print(f'#{tc}')
    print(*money_cnt)