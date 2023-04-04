# 재귀를 사용했을 때
def dfs1(v,k): # k개의 정점
    visited[v] = 1 # 중복방지용
    print(v)

    # 인접 리스트를 사용할 때
    for w in adjL(v): # v와 인접하고
        if visited[w] == 0: # 방문한적이 없는 w가 있으면
            dfs1(w, k)

    # 인접 행렬을 사용할 때
    for w in range(1, k+1):
        if adjM[v][w] == 1 and visited[w] == 0:
            dfs1(w, k)

# 재귀를 사용하지 않고 stack사용
def dfs2(s,k):
    stack = []
    visited = [0] * (k+1)
    v = s
    while True:
        if visited[v] == 0:
            print(v)
            visited[v] = 1
        for w in range(1, K+1):
            if adjM[v][w] and visited[w] == 0:
                stack.append(v)
                v = w
                break
        else: # 더 이상 인접 정점이 없으면
            if stack: # 스택이 비어있지 않으면
                v = stack.pop()
            else: # 스택이 비어있으면
                break
    return

def dfs3(v,k,g):  # g 목적지
    giobal cnt
    if v == g:
        cnt += 1 # 목적지 도착횟수
    else:
        visited[v] = 1 # 중복방지용

        # 인접 리스트를 사용할 때
        for w in range(1,k+1):  # v와 인접하고
            if adjM[v][w] == 1 and visited[w] == 0:  # 방문한적이 없는 w가 있으면
                dfs1(w, k, g)
        visited[v] = 0 # 또 다른 경로로도 들어올 수 있도록 열어줌

