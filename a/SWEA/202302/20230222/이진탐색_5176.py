import sys
sys.stdin = open('input', 'r')
def in_order(node):
    if node != 0:
        in_order(tree[node][0])
        number.append(node)
        in_order(tree[node][1])
    return number


T = int(input())
for tc in range(1,T+1):
    v = int(input())
    e = v-1
    number = []
    tree = [[0 for _ in range(3)] for _ in range(v+1)]
    #왼쪽자식 오른쪽 자식 부모
    for i in range(1,v//2+1):
        if i*2>v:
            break
        else:
            tree[i][0] = i*2
        if i*2+1>v:
            break
        else:
            tree[i][1] = i*2+1
        tree[i][2] = i//2

    for idx,numb in enumerate(in_order(1)):
        if numb == 1:
            a = idx+1
        if numb == v//2:
            b = idx+1

    print(f'#{tc}',a,b)