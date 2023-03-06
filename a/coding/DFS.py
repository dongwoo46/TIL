graph =[
    [],
    [2,3],
    [4,5],
    [1,7],
    [2,6],
    [2,6],
    [4,5,7],
    [6,3]
]
visited = [False]* len(graph)

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph,1,visited)