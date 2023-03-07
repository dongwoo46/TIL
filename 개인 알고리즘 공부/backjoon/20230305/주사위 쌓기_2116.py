import sys
sys.stdin = open('../20230305/input', 'r')
n = int(input())
li = [list(map(int, input().split())) for i in range(n)] + [[1,2,3,4,5,6]] # 주사위들의 2차원 리스트


high = 0
com = 0  # 윗면의 수
for k in range(6):  # 첫 주사위의 밑면이 될 인덱스 k
    total = 0  # 밑면이 바뀔 때 마다 최대합을 담을 변수
    i = 0  # 탐색 할 주사위 인덱스
    while i != n:  # 종료 조건
        if k == 0:
            total += max(li[i][1], li[i][2], li[i][3], li[i][4])
            # 밑면과 윗면을 제외한 면들 중 최대 값을 더함
            com = li[i][5]  # 윗면담기
            i += 1  # 다음 주사위
            k = li[i].index(com)  # 다음 주사위의 밑면이 됨

        elif k == 5:
            total += max(li[i][1], li[i][2], li[i][3], li[i][4])
            com = li[i][0]
            i += 1
            k = li[i].index(com)

        elif k == 1:
            total += max(li[i][0], li[i][2], li[i][4], li[i][5])
            com = li[i][3]
            i += 1
            k = li[i].index(com)

        elif k == 3:
            total += max(li[i][0], li[i][2], li[i][4], li[i][5])
            com = li[i][1]
            i += 1
            k = li[i].index(com)

        elif k == 2:
            total += max(li[i][0], li[i][1], li[i][3], li[i][5])
            com = li[i][4]
            i += 1
            k = li[i].index(com)

        elif k == 4:
            total += max(li[i][0], li[i][1], li[i][3], li[i][5])
            com = li[i][2]
            i += 1
            k = li[i].index(com)

    if total > high:
        high = total

print(high)
