import sys
sys.stdin = open('input','r')
# 1 N극(빨강) 2 S극(파랑) ->시작하는 번호 2이어야함 끝은 1
for tc in range(1,11):
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(100)]
    arr = [[board[j][i] for j in range(100)] for i in range(100)]
    cnt = 0
    check = []
    for i in range(100):
        for j in range(100):
            if arr[i][j]!=0:
                check.append(arr[i][j])

        while check[0] == 2:
            check.pop(0)
        while check[-1] == 1:
            check.pop()

    for k in range(len(check)-1):
        if check[k] ==1 and check[k+1]== 2:
            cnt+=1

    print(f'#{tc} {cnt}')
