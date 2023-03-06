import sys
sys.stdin = open('input', 'r')

delta = [(1,0),(0,1),(-1,0),(0,-1)]
def bfs(x,y,cnt): #x좌표,y좌표, 몇칸 이나 이동했는가
    q = [(x,y,cnt)] #q에 x,y,cnt값을 집어넣는다. cnt는 몇칸 이동했는지에 대한 값이다.
    while q: # q가 남아있다면 dequeue를 한다.
        x,y,cnt = q.pop(0)
        # print(t, end = '')
        for dx,dy in delta: # 4방향으로 돌면서
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<n: # 만약 nx,ny가 미로의 범위를 벗어나지 않고
                # graph의 좌표값이 0이면 1로 변경해준뒤 cnt에 1을 더한다.
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    q.append((nx,ny,cnt+1))
                    # 만약 graph의 값이 3이면 cnt를 리턴받는다.
                elif graph[nx][ny] == 3:
                    return cnt
    return 0


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    graph = [list(map(int,input())) for _ in range(n)]
    res = 0
    for x in range(n):
        for y in range(n):
            if graph[x][y] == 2:
                res = bfs(x,y,0)


    print(f'#{tc}', res)


