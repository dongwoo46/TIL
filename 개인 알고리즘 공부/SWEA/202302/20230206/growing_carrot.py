# def maximum(arr):
#     max_v = arr[0]
#     for i in range(len(arr)-1):
#         if max_v <= arr[i]:
#             max_v = arr[i]
#     return max_v

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    carrot = list(map(int,input().split()))
    max_cnt = 1
    cnt = 1
    for i in range(N-1):
        if carrot[i] > carrot[i+1]:
            cnt = 1
        else:
            cnt +=1
            if max_cnt<cnt:
                max_cnt = cnt


    print(f'#{tc} {cnt}')


