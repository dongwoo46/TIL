import sys
sys.stdin = open('input', 'r')
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cost = list(map(int, input().split()))
    max_cost = 0
    income = 0
    for i in range(n-1,-1,-1):
        if cost[i] > max_cost:
            max_cost = cost[i]
        else:
            income += max_cost - cost[i]
    print(f'#{tc}',income)