T = int(input())
for tc in range(1,T+1):
    n = int(input())
    ans_list = [0] * 1001
    cnt = 0
    for _ in range(0,n):
        bus_route = list(map(int, input().split()))
        ans_list[bus_route[1]]=1
        ans_list[bus_route[-1]]=1

        if bus_route[0] == 1:
            for i in range(bus_route[1]+1, bus_route[-1]):
                ans_list[i] += 1

        if bus_route[0] == 2:
            for j in range(bus_route[1]+1, bus_route[-1]):
                if bus_route[1]%2 == 0:
                    if j%2 == 0:
                        ans_list[j] += 1
                else:
                    if j % 2 == 1:
                        ans_list[j] += 1
        if bus_route[0] == 3:
            for k in range(bus_route[1]+1,bus_route[-1]):
                if bus_route[1]%2 == 0:
                    if k % 4 == 0:
                        ans_list[k] += 1
                else:
                    if bus_route[1]%2 == 1:
                        if k % 3 == 0 and k % 10 != 0:
                            ans_list[k] += 1


    print(f'#{tc} {max(ans_list)}')
