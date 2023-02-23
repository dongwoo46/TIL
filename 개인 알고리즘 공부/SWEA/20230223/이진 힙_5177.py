import sys
sys.stdin = open('input','r')
def enq(v):
    global last
    last +=1
    heap[last] = v
    c = last
    p = c//2
    while p>0 and heap[p] > heap[c]:
        heap[p],heap[c] = heap[c],heap[p]
        c = p
        p = c//2
    return

# def get_sum(tree):
#     p_node = v//2
#     p_sum = 0
#     while tree[p_node]:
#         p_sum += tree[p_node]
#         p_node = p_node//2
#     return p_sum


T = int(input())
for tc in range(1,T+1):
    heap = [0]*501
    last = 0 #노드의 번호
    total = 0
    v = int(input())
    numb = map(int,input().split())
    for i in numb:
        enq(i)
    print(heap)

    while v!=1:
        v = v//2
        total += heap[v]
    print(f'#{tc}', total)