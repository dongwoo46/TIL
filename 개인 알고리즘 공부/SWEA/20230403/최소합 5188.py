import sys
sys.stdin = open('input','r')
def perm(i,k):
    if i== k:
        print(p)
    else:
        for j in range(k): # 사용하지 않는 숫자를
            if used[j] == 0: # used에서 순서대로 검색
                p[i] = a[j]
                used[j] = 1 # j번째 숫자 사용으로 표시
                perm(i+1,k)
                used[j] = 0


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    a =
    p = [0]*(2*(n-1))
    used = [0]*(2*(n-1))
    perm(0,4)