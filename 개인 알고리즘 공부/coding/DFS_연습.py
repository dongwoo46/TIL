visited = [False] * 8
stack = []

graph = [[0]*8 for _ in range(8)]

n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

res= []
v = 1
visited[v] = True
res.append(v)

while True:
    found = False
    #v에서 출발하고 도착하는 점이 w가 1이고 visied가 False이면
    for w in range(8):
        if graph[v][w] == 1 and visited[w] == False:
            stack.append(v)
            v = w
            visited[w] = True #w에 방문함
            res.append(w)
            found = True
            break
    if not found: # found가 false이면
        if stack:
            v = stack.pop()
        else: #스택이 비어있으면
            break

print(''.join(map(str,res)))

