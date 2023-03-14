def n_queens(i): # i는 행번호
    global ans
    if i == n:
        ans += 1
        return
    else:
        for j in range(n):
            # 행 렬 대각선방향에 이미 들어간 게 있는지 없는지 체크
            if v1[j]==v2[j+i]==v3[j-i]==0:
                v1[j] = v2[j + i] = v3[j - i] = 1
                n_queens(i+1)
                v1[j] = v2[j + i] = v3[j- i] = 0


n= int(input())
ans = 0
v1,v2,v3 = [[0]*(2*n) for _ in range(3)]
n_queens(0)
print(ans)