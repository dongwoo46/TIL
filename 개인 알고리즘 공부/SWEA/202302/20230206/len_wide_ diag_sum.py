import sys
sys.stdin = open("input", "r")


for _ in range(1,11):
    t = int(input())
    hund_map = []
    for i in range(100):
        first_map = list(map(int, input().split()))
        hund_map.append(first_map)


    length_max = 0
    wide = 0
    diagnol1 = 0
    diagnol2 = 0

    #가로 합
    for i in hund_map:
        if wide <= sum(i):
            wide = sum(i)

    #세로합
    for i in range(100):
        length = 0
        for j in range(100):
            length += hund_map[j][i]
        if length >= length_max:
            length_max = length
    #대각선 합 좌->우
    for i in range(100):
        for j in range(100):
            if i == j:
                diagnol1 += hund_map[i][j]

    #대각선 합 우->좌
    for i in range(100):
        for j in range(99,-1,-1):
            if i+j == 100:
                diagnol2 += hund_map[i][j]


    ans = max(diagnol2, diagnol1, length_max, wide)
    print(f'#{t} {ans}')

