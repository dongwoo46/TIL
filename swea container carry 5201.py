import sys
sys.stdin =open('input')
import time
from itertools import combinations


start = time.time()
T = int(input())

for tc in range(1, T+1):
    n,m = map(int,input().split())
    contain = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    contain.sort(reverse=True)
    truck.sort()
    visited = [0]*len(truck)
    ans = 0
    for c in contain:
        for i in range(len(truck)):
            if visited[i] == 0 and truck[i]>=c:
                ans +=c
                visited[i] = 1
                break
    print(f'#{tc}', ans)
print(time.time()-start)