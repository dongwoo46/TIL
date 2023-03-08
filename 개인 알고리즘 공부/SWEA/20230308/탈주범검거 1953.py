import sys
sys.stdin = open('input','r')

delta1 = [(-1,0),(1,0),(0,-1),(0,1)]
delta2 = [(-1,0),(1,0)]
delta3 = [(0,-1),(0,1)]
delta4 = [(-1,0),(0,1)]
delta5 = [(0,1),(1,0)]
delta6 = [(0,-1),(1,0)]
delta7 = [(-1,0),(0,-1)]
dic = {1:delta1,2:delta2,3:delta3,4:delta4,5:delta5,6:delta6,7:delta7}

#범위체크 함수
def is_valid(x,y):
    return 0<=x<n and 0<=y<m
#탈출범이 갈 수 있는 곳을 bfs를 이용하여 카운트해줌
def escape(x,y):
    # 시작점을 q에 넣고 1시간이 지난후에 출발하니까 visited[x][y]에 1을 넣어줌 여기서 visited 값은 탈출범이 탈출한지 시간을 체크하는 용도 겸 방문확인!!
    q = [(x,y)]
    visited[x][y] = 1
    # q가 있으면 계쏙 반복함
    while q:
        #만약 visited에서 max값이 l을 초과하면 반복 종료
        for i in visited:
            if max(i)> l:
                return visited
        # bfs 실행
        x,y= q.pop(0)
        for dx,dy in dic[board[x][y]]:
            nx = x+dx
            ny = y+dy
            # 보드가 0이아니고 범위를 벗어나지 않으면 시작
            if is_valid(nx,ny) and board[nx][ny]!=0:
                # 또한 nx,ny로 움직였을 때 해당 board가 x,y에서의 보드와 서로 연결되는지 확인하기 위해
                # board[nx][ny]의 dic을 이용하여 방향을 돌면서 확인햇을때
                for dx,dy in dic[board[nx][ny]]:
                    a = nx +dx
                    b = ny + dy
                    # x,y가 나오면 연결된것
                    if x==a and y==b:
                        # visited가 0이면 visited에 이전 visited값 +1 을 해서 넣어줌 (시간체크 겸 방문확인)
                        if visited[nx][ny] == 0:
                            visited[nx][ny] = visited[x][y]+1
                            q.append((nx,ny))
    return visited




T = int(input())
for tc in range(1,T+1):
    n,m,r,c,l = list(map(int,input().split()))
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    ans = 0

    result = escape(r,c)
    # vistied를 돌면서 visited값이 1과 l사이에 잇으면 ans에 1을 더해줌
    for i in range(n):
        for j in range(m):
            if result[i][j]<=l and result[i][j]>0:
                ans+=1
    print(f'#{tc}', ans)