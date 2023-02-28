
T = int(input())

for _ in range(T):
    arr = input() # 문자열로 입력
    for i in range(0, len(arr), 7): # 7글자씩 확인
        print(int(arr[i:i+7],2), end=' ')
    print()
    # l = len(arr) // 7
    #
    # for i in range(l): # 0, 1, 2, ...
    #     res = 0
    #     n = 64
    #     for j in range(i*7, (i+1)*7): # 0~6, 7~13, 14~20
    #         if arr[j]:
    #             res += n
    #         n = n >> 1
    #     print(res, end=' ')
    # print()