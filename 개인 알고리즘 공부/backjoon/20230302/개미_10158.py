import sys
sys.stdin = open('input','r')

w, h = map(int,input().split())
p, q = list(map(int,input().split()))
t = int(input())
time = 0
direction = 0
delta = [(1,1),(-1,1),(-1,-1),(-1,1)]

while time!=t:
    if t:
    np = p + delta[direction][0]
    nq = q + delta[direction][1]
    if 0 <= np < w + 1 and 0 <= nq < h + 1:
        p = np
        q = nq
        time += 1
    else:
        direction = (direction + 1) % 4



print(p,q)
