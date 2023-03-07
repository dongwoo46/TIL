import sys
sys.stdin = open('input', 'r')
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    room = [list(map(int,input().split())) for _ in range(n)]
    route = [0]*200
    for r in room:
        if r[0]<r[1]:
            for i in range((r[0]-1)//2,(r[1]-1)//2+1):
                route[i] += 1
        elif r[0] == r[1]:
            continue
        else: #r[0] >r[1]
            for i in range((r[1]-1)//2,(r[0]-1)//2+1):
                route[i] += 1
    print(f'#{tc} {max(route)}')
