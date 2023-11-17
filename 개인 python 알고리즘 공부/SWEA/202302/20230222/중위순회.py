import sys
sys.stdin = open('input', 'r')
# sys.setrecursionlimit(10**7)

def in_order(node):
    if node:
        in_order(tree[node][0])
        print(tree[node][2], end= '')
        in_order(tree[node][1])

for tc in range(1,11):
    v = int(input())
    e = v-1
    tree = [[0 for _ in range(4)] for _ in range(v+1)]

    # 정점 정점데이터 왼쪽자식 오른쪽자식
    #tree 왼쪽자식, 오른쪽자식, data, 부모
    for i in range(v):
        temp = list(map(str,input().split()))

        if len(temp)==4:
            tree[int(temp[0])][0] = int(temp[2])
            tree[int(temp[0])][1] = int(temp[3])
            tree[int(temp[3])][3] = int(temp[0])
            tree[int(temp[2])][3] = int(temp[0])
            tree[int(temp[0])][2] = temp[1]
        elif len(temp)==3:
            tree[int(temp[0])][0] = int(temp[2])
            tree[int(temp[2])][3] = int(temp[0])
            tree[int(temp[0])][2] = temp[1]
        # elif len(temp) == 2:
        #     tree[int(temp[0])][2] = temp[1]
        else:
            tree[int(temp[0])][2] = temp[1]


    print(f'#{tc}', end=' ')
    in_order(1)
    print()



