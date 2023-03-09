import sys
sys.stdin = open('input','r')
delta = [(-1,0),(1,0),(0,-1),(0,1)]
delta_cross = [(-1,-1),(-1,1),(1,-1),(1,1)]
def counting_house(x,y):
    global mx
    house = 0
    s = e = y
    k = 1
    while True:
        if k>2*n:
            return mx
        if k == 1 and board[x][y] ==1:
            house+=1
            if m * house >= 2 * (k ** 2) + 2 * k + 1:
                mx = max(house, mx)
                k += 1
            continue
        else:
            for i in range(x-k+1,x+k):
                for j in range(s, e + 1):
                    if 0<=i<n and 0<=j<n and board[i][j] == 1:
                        house +=1
                    else:
                        continue
                # 행의 인덱스가 mid 전까지는 s-e 간격 늘리고 mid 이후로는 간격 줄임

                if i < x:
                    s -= 1
                    e += 1
                else:
                    s += 1
                    e -= 1
            if (k*k+((k-1)*(k-1)))<=m*house:
                mx = max(house, mx)
        k += 1







T = int(input())
for tc in range(1,T+1):
    n,m = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]
    mx = 0
    result =0
    for x in range(n):
        for y in range(n):
            ans = counting_house(x,y)
            result = max(ans,result)

    print(f'#{tc}', result)




