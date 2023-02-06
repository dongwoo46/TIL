import sys
sys.stdin = open("input", "r")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ten_map = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        paint = list(map(int, input().split()))
        start_location = [paint[0], paint[1]]
        end_location = [paint[2], paint[3]]

        for j in range(start_location[0],end_location[0]+1):
            for k in range(start_location[1], end_location[1]+1):
                ten_map[j][k] +=1

    for color in ten_map:
        for j in color:
            if j>=2:
                cnt+=1

    print(f'#{tc} {cnt}')

#누적합 imos법으로 풀면 조흠


