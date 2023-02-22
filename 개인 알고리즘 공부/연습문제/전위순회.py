import sys
sys.stdin = open('input','r')

v = int(input())
e = v-1
tree = [[0 for _ in range(3)] for i in range(v+1)]
temp = list(map(int, input().split()))

#전위 순회
def pre_order(node):
    if node != 0:
        print(f'{node}', end=' ')
        pre_order(tree[node][0]) #왼쪽자식
        pre_order(tree[node][1]) #오른쪽자식

#중위순회
def in_order(node):
    if node:
        in_order(tree[node][0])
        print(f'{node}', end=' ')
        in_order(tree[node][1])

#후위 순회
def post_order(node):
    if node:
        post_order(tree[node][0])
        post_order(tree[node][1])
        print(f'{node}',end=' ')

for i in range(e):
    p, c = temp[i*2], temp[i*2+1]
    #왼쪽자식 오른쪽자식 부모 순으로 트리에 집어넣음음
    if not tree[p][0]:
        tree[p][0] = c
    else:
        tree[p][1] = c

    tree[c][2] = p

pre_order(1) #1 2 4 7 12 3 5 8 9 6 10 11 13
print()
in_order(1)
print()
post_order(1)

#
# [[0, 0, 0],
#  [2, 3, 0],  1번 노드의 정보 tree[1]
#  [4, 0, 1],
#  [5, 6, 1],
#  [7, 0, 2],
#  [8, 9, 3],
#  [10, 11, 3],
#  [12, 0, 4],
#  [0, 0, 5],
#  [0, 0, 5],
#  [0, 0, 6],
#  [13, 0, 6],
#  [0, 0, 7],
#  [0, 0, 11]]
