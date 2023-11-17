import heapq
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
h = []
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(h, -x)
    else:
        if not h:
            print(0)
        else:
            print(-heapq.heappop(h))