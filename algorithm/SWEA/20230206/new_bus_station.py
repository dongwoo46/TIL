def maximum(arr):
    max_v = arr[0]
    for i in range(len(arr)-1):
        if max_v <= arr[i]:
            max_v = arr[i]
    return max_v


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    ans_list = [0] * 1001
    cnt = 0

    for _ in range(0,n):
        bus_route = list(map(int, input().split()))
    # normal_list = [0] * (normal[-1]+1) #6개
    # express_list = [0] * (express[-1]+1) #11개
    # board_list = [0] * (board[-1]+1) # 10개


        if bus_route[0] == 1:
            for i in range(bus_route[1], bus_route[-1]+1):
                ans_list[i] += 1


        if bus_route[0] == 2:
            for j in range(bus_route[1], bus_route[-1]+1):
                if bus_route[1]%2 == 0:
                    if j%2 == 0:
                        ans_list[j] += 1

                else:
                    if j % 2 == 1:
                        ans_list[j] += 1
        if bus_route[0] == 3:
            for k in range(bus_route[1],bus_route[-1]+1):
                if bus_route[1]%2 == 0:
                    if k % 4 == 0:
                        ans_list[k] += 1
                else:
                    if bus_route[1]%2 == 1:
                        if k % 3 == 0 and k % 10 != 0:
                            ans_list[k] += 1


            # for i in range(normal[1], normal[-1]+1):
            #     normal_list[i] = 1
            #
            # for j in range(express[1], express[-1]+1):
            #     if express[1]%2 == 0:
            #         if j%2 == 0:
            #             express_list[j] = 1
            #     else:
            #         if j % 2 == 1:
            #             express_list[j] = 1
            #
            # for k in range(board[1],board[-1]+1):
            #     if board[1]%2 == 0:
            #         if k % 4 == 0:
            #             board_list[k] = 1
            #     elif board[1]%2 == 1:
            #         if k % 3 == 0 and k % 10 != 0:
            #             board_list[k] =1

            # for i in range(len(normal_list)):
            #     if normal_list[i] == 1:
            #         ans_list[i] += 1
            #
            # for i in range(len(board_list)):
            #     if board_list[i] == 1:
            #         ans_list[i] += 1
            #
            # for i in range(len(express_list)):
            #     if express_list[i] == 1:
            #         ans_list[i] += 1


    print(f'#{tc} {maximum(ans_list)}')

#출발점 종점 따로 ans_list에 넣어줌
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