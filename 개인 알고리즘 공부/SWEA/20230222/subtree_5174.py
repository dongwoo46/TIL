import sys
sys.stdin = open('input','r')

def pre_order(node):
    global cnt
    if node:
        cnt +=1
        pre_order(tree[node][0])
        pre_order(tree[node][1])
    return cnt

T = int(input())
for tc in range(1,T+1):
    e, n = list(map(int,input().split()))
    v = e+1
    cnt = 0
    tree = [[0 for i in range(3)] for _ in range(v+1)]
    temp = list(map(int,input().split()))
    #왼쪽자식 오른쪽자식 부모
    for i in range(e):
        p,c = temp[i*2], temp[i*2+1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    print(f'#{tc}',pre_order(n))

