import sys
sys.stdin =open('input')
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    schedule = [list(map(int,input().split())) for _ in range(n)]
    schedule.sort(key = lambda x:x[1])

    cnt = 0

    for i in range(n-1):
        result = []
        result.append(schedule[i])
        for j in range(i+1,n):
            if result[-1][1]<=schedule[j][0]:
                result.append(schedule[j])
                i = j
        cnt = max(cnt,len(result))

    print(f'#{tc} {cnt}')



