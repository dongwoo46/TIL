import sys
sys.stdin = open("input", "r")

T = int(input())

for tc in range(1, T+1):
    k, n, m = list(map(int, input().split()))
    stop_numb = list(map(int, input().split()))
    now = 0
    move = now + k
    station = 0
    cnt = 0

    while move < n:
        for stop in stop_numb:
            if now < stop <= move:
                station = stop
            elif move < stop:
                break
        if station == -1:
            cnt = 0
            break
        now = station
        move = now + k
        cnt += 1
        station = -1

    print(f"#{tc} {cnt}")

    # for i in range(m):
    #     if location + k != n:
    #         while stop_numb[i]< location+(i+1)*k<stop_numb[i+1]:
    #             location
    #
    #     while stop_numb[i+1] >= location+k and (location + k) !=n:
    #         cnt += 1
    #         location = stop_numb[i]
    #         if location + k == n:
    #             break
    #
    #
    #                 # if location + i*k != n:
    #                 #     location = stop_numb[i]
    #                 #     cnt +=1
    #                 # else:
    #                 #     break
    #                 # if stop_numb[i+1] >= location + i*k :
    #                 #     cnt += 1
    #                 #     location = stop_numb[i+1]
    #                 # elif stop_numb[i+1] > location + k and stop_numb[i] <= location+k:
    #                 #     cnt += 1
    #                 #     location = stop_numb[i]
    #             #마지막 충전기 정류장일 때
    #         #     else:
    #         #         if location + k >= n:
    #         #             continue
    #         #         else: # location + k < n:
    #         #             cnt +=1
    #         #             location = stop_numb[n//k]
    #         #             if location+k>=n:
    #         #                 continue
    #         #             else:
    #         #                 cnt = 0
    #         # elif location + i*k>stop_numb[i+1]:
    #         #     cnt = 0
    #
    #     print(f'#{tc} {cnt}')
    #
    #
    #
    #
