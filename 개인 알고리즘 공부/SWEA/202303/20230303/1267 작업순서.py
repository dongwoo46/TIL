import sys
sys.stdin = open('input', 'r')

def search():
    global order
    # 만약 그래프의 모든 리스트가 텅 비어있으면 종료
    while True:
        if all_clear():
            break
        # graph를 반복해서 탐색한다 만약 graph안이 비어있거나 visited가 0일때
        for k in range(1, v+1):
            if not graph[k] and visited[k] == 0:
                # 그래프안의 모든 리스트에  k의 값들을 삭제
                for j in range(1,v+1):
                    if k in graph[j]:
                        graph[j].remove(k)
                # visited[k]에 order를 넣음 order는 탐색하는 순서이다
                visited[k] = order
                order+=1
                break
    return visited

# 만약 그래프의 모든 것이 비어있을 때 False return 하고 반복 종료
def all_clear():
    for i in range(1,v+1):
        if graph[i]:
            return False

    else:
        # 만약 그래프 안이 다비어서 반복문을 다 종료했지만 visited에 아직 0이
        #남아 있을 때 visited에는 visited의 max값에 1을 더해서 계속 넣어서 꽉채워줌
        for k in range(1,v+1):
            if visited[k] == 0:
                visited[k] = max(visited)+1
        return True

for tc in range(1,11):
    v, e = list(map(int,input().split()))
    node = list(map(int,input().split()))
    # 그래프를 만든다.
    graph = [[] for _ in range(v+1)]
    visited =[-1] + [0]*(v)
    order = 1
    # 그래프의 인덱스를 기준으로 해당 인덱스 번호를 실행하기 위해서 어떤 번호가 끝나면
    # 그 번호르 실행할 수 잇는지 그래프안에 집어넣음
    for i in range(e):
        a,b = node[i*2],node[i*2+1]
        graph[b].append(a)



    result_list = search()
    ans_list = []
    for idx,value in enumerate(result_list):
        ans_list.append((idx,value))

    ans_list.sort(key = lambda x:x[1])
    print(f'#{tc}', end=' ')
    for i in range(1, len(ans_list)):
        print(ans_list[i][0], end=' ')
    print()








