from collections import deque
import sys
sys.stdin = open('input', 'r')
n = int(input())
deq= deque(x for x in range(1,n+1))

while len(deq) !=1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])