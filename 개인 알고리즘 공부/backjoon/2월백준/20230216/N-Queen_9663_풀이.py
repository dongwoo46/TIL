import sys

n = int(sys.stdin.readline().rstrip())

ans = 0
row = [0] * n


def is_promising(x):
    for i in range(x):
        print(f'is_promising의 i값', i)
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1 #칸마다 안겹치고 퀸을 놓을 수 있는 횟수
        print(f'row는',row)

    else:
        for i in range(n): # 열의 위치를 정한다.

            print(f'x는',x)
            row[x] = i # [x, i]에 퀸을 놓겠다.
            if is_promising(x): #열과 대각선이 같은지  안 같은지 확인 => 같으면 False 안 같으면 True
                n_queens(x + 1) # 같지 않으면 x(행의 좌표) 한칸 더내려가서 dfs 재귀


n_queens(0)
print(ans)