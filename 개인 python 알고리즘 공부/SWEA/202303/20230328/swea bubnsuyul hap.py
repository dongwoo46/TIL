import sys

sys.stdin = open('../../../../input')
#
# from itertools import combinations
#
# T = int(input())
# for tc in range(1,T+1):
#     n, k = map(int,input().split())
#     arr = list(map(int,input().split()))
#     result = []
#
#     cnt = 0
#     for i in range(len(arr)+1):
#         total = 0
#         result = list(combinations(arr, i))
#         for i in range(len(result)):
#             if sum(result[i]) == k:
#                 cnt+=1
#
#     print(f'#{tc}' ,cnt)

def f(i, k):
    global cnt
    if i == k: # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += arr[j]

        if s == t:
            cnt+=1

    else:
        # 비트 i = 1일때 탐색
        bit[i] = 1
        f(i + 1, k)
        # 비트 i = 0 일때 탐색
        bit[i] = 0
        f(i + 1, k)

T = int(input())
for tc in range(1,T+1):
    n, t = map(int,input().split())
    arr = list(map(int,input().split()))
    result = []
    cnt = 0
    bit = [0] * len(arr)
    f(0,len(arr))

    print(f'#{tc}', cnt)
