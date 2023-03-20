import sys

sys.stdin = open('input', 'r')

board = [list(map(int,input().split())) for _ in range(5)]
bingo = [list(map(int,input().split())) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
#상하좌우 대각선 모두 체크할 필요 x -> 하, 우, 하우대각,하좌대각 확인
delta = [(1,0),(0,1),(1,1),(1,-1)]
ans_cnt = 0
# 범위 체크
def is_valid(x,y):
    return 0<=x<5 and 0<=y<5

# 빙고 줄이 3개인지 확인
def check_bingo():
    # 빙고를 모든 곳을 방문하는데 만약 visited가 1인 아닌 부분은 그냥 넘어감
    # cnt는 빙고줄 수
    cnt = 0
    for x in range(5):
        for y in range(5):
            if visited[x][y] == 1:
                # 델타를 이용해 계속 돌면서 해당 방향으로 5번 반복해서 5칸 연속으로 visited가 1인지 확인
                for dx,dy in delta:
                    for i in range(5):
                        nx = x + dx*i
                        ny = y + dy*i
                        # 만약 범위를 벗어나거나 1이 아니면 종료
                        if not is_valid(nx,ny) or visited[nx][ny] != 1:
                            break
                    # for-else구문 5번 다 중간에 종료없이 다 돌면 5칸이 연속으로 1이기 때문에 cnt +1
                    else:
                        cnt +=1
            # cnt가 1이면 true 출력
            if cnt >= 3:
                return True


# 사회자가 부른 빙고판을 순서대로 돌면서 빙고 번호와 보드판의 값과 일치하면 해당 좌표의 visited에 1을 넣음
ans = 0
for i in range(5):
    for j in range(5):
        ans_cnt +=1
        for m in range(5):
            for n in range(5):
                if bingo[i][j] == board[m][n]:
                    visited[m][n] = 1

                    #만약 빙고가 된다면
                    if check_bingo():
                        # 해당 보드의 좌표값 ans 에 저장
                        ans = ans_cnt
                        break
            if ans:
                break
        if ans:
            break
    if ans:
        break
#출력
print(ans)
