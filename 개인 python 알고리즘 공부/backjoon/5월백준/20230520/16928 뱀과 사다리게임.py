import sys
from collections import deque
sys.stdin = open('input', 'r')

ladder = {}
snake = {}
cnt = 0
n,m = map(int,input().split())

for _ in range(n):
    a,b = map(int,input().split())
    ladder[a] = b
# print(ladder)

for _ in range(m):
    c,d = map(int,input().split())
    snake[c] = d
# print(snake)

visited = [0]*101
backladder = {value:key for key,value in ladder.items()}
backsnake = {value:key for key,value in snake.items()}
cnt = [0]*101

q = deque()
q.append(1)

while q:
    now = q.popleft()
    if now == 100:
        print(cnt[100])
        break

    for i in range(1,7):
        next = now + i
        if next<=100 and not visited[next]:
            if next in ladder:
                next = ladder[next]
            if next in snake:
                next = snake[next]
            if not visited[next]:
                visited[next] = 1
                cnt[next] = cnt[now] + 1
                q.append(next)




# def move(v):
#     if v in ladder:
#         v = ladder[v]
#         return
#     elif v in snake:
#                 v = snake[v]
#                 return
#     else:
#         v = v
#         return
#
# def backmove(v):
#     if v in backladder:
#         v = backladder[v]
#     elif v in backsnake:
#         v = backsnake[v]
#         return
#
# def backtracking(v,now):
#     global cnt
#     if now == 100:
#         return cnt
#     if v>100:
#         return cnt
#     for i in range(1,7):
#         now += i
#         cnt+=1
#         move(now)
#         backtracking(v+1,now)
#         backmove(now)
#         cnt-=1
#         now -=i
#
# print(backtracking(0, 1))
