import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    # min_total = 1000000000
    # for i in range(n-1):
    #     total = 0
    #     for j in range(n):
    #         if visited[i]:
    #             visited[i][j] = 1
    #             total += board[i][j]
    #             a = j
    #         if visited[i+1][j] == 0 and a!=j:
    #             visited[i+1][j] = 1
    #             total += board[i+1][j]
    #
    #     if min_total > total:
    #         min_total = total
    #
    # print(f'{tc} {min_total}')

def f(i,k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1,k)


bit = [0]* 3