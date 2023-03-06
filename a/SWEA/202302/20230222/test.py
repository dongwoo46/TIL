import sys
sys.stdin = open('input')

# 전위순회 VLR
def pre_order(node):
    if node != 0:
        print(f'{node}', end=' ')
        pre_order(tree[node][0]) # 왼쪽 자식
        pre_order(tree[node][1]) # 오른쪽 자식

# 중위 순회 LVR
def in_order(node):
    if node != 0:
        in_order(tree[node][0]) # 왼쪽 자식
        print(f'{node}', end=' ')
        in_order(tree[node][1]) # 오른쪽 자식
# 후위 순회 LRV
def post_order(node):
    if node != 0:
        post_order(tree[node][0]) # 왼쪽 자식
        post_order(tree[node][1]) # 오른쪽 자식
        print(f'{node}', end=' ')


V = int(input())
E = V - 1

tree = [[0 for _ in range(3)] for _ in range(V+1)]

temp = list(map(int, input().split()))

for i in range(E):
    p, c = temp[i*2], temp[i*2+1]
    if not tree[p][0]:
        tree[p][0] = c
    else:
        tree[p][1] = c

    tree[c][2] = p
    # [2, 3, 0], 1번 노드의 정보 tree[1]
    # [4, 0, 1], 2번 노드 tree[2]

# print(tree)
pre_order(1) # 1 2 4 7 12 3 5 8 9 6 10 11 13
# print()
# in_order(1) #
# print()
# post_order(1) #