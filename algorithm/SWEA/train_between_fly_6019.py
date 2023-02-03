T = int(input())
for tc in range(1, T+1):
    d, a, b, f = list(map(int,input().split()))
    #a = a기차속력
    #b = b 기차 속력
    #d = 기차사이 거리
    #f = 파리 속력
    time = d/(a+b)
    fly_dis = time * f
    print(f'#{tc} {fly_dis}')
