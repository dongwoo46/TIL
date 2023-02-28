

def f(start, depth):
    if depth == 6:   #하나의 부분집합 완성
        print(*result)
        return

    for i in range(start, k):
        if not visited[i]:
            result[start] = s[i]
            visited[i] = 1
            f(start+1,i+1)
            visited[i] = False

while True:
    list1 = list(map(int,input().split()))
    k = list1[0]
    if k == 0:
        exit()
    s = list1[1:]
    visited = [0] * k
    result = [0] * 6
    f(0,0)
    print()


# import sys
# input = sys.stdin.readline
#
# def comb(depth, pos):
#     if depth == 6:
#         print(*order)
#         return
#     for i in range(pos, k):
#         order.append(lottos[i])
#         comb(depth+1, i+1)
#         order.pop()
#
# while True:
#     lottos = list(map(int, input().split()))
#     k = lottos.pop(0)
#     if not lottos:
#         break
#     order = []
#     comb(0, 0)
#     print()
