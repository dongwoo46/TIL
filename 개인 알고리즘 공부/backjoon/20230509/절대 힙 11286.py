import heapq
import sys

input = sys.stdin.readline
h = []

n = int(input())
for _ in range(n):
    numb = int(input())
    if numb:
        heapq.heappush(h,(abs(numb),numb))
    else:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
