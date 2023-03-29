# 백준 이중 우선순위큐

import sys
import heapq
sys.stdin = open('input')
input = sys.stdin.readline
mx = 0
mn = 1e9
T = int(input())
n = int(input())
h = [] #최소힙
h_max = [] #최대힙
used = [0]*2000000
for i in range(n):
    order, numb = input().split()
    numb = int(numb)

    if order == "I": # heapq에 숫자 인풋하기
        heapq.heappush(h, numb)
        heapq.heappush(h_max, -numb)
    else:
        if len(h) !=0:
            if order == "D" and numb==1:# heapq에서 최소 값 뽑아내기
                if h[0]<0:
                    if used([abs(h[0])+1000000]) == 0:

                a = heapq.heappop(h)
                if a<0:
                    used[abs(a)+1000000] = 1
                else:
                    used[a] = 1

            elif order == "D" and numb== -1: #heapq에서 최대값 뽑아내기
                b = -heapq.heappop(h_max)
                if b<0:
                    used[abs(b)+1000000] = 1
                else:
                    used[b] = 1

        else:
            if order=="D":
                print('EMPTY')
                exit()

for i in h:
    if i not in used:
        mx = max(mx, i)
        mn = min(mn,i)
print(mx,mn)
