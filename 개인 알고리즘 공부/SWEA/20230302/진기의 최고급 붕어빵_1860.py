import sys
sys.stdin = open('input','r')


T = int(input())
for tc in range(1,T+1):
    # n 손님수 , m 붕어빵만드는시간 , k m초동안 만드는 붕어빵 수
    n,m,k = list(map(int,input().split()))
    guest = list(map(int,input().split()))
    guest.sort(reverse=True)
    cnt = 0
    time = 0
    bread = 0
    ans = 'Impossible'
    while True:
        if not guest:
            ans = 'Possible'
            break

        if bread == m:
            cnt+=k
            bread = 0

        if cnt >= 11111:
            ans = 'Possible'
            break


        if time == guest[-1]:
            if cnt ==0:
                ans = 'Impossible'
                break
            else:
                cnt -=1
                guest.pop()

        time += 1
        bread +=1

    print(f'#{tc}', ans)
