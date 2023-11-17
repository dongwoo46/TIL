from collections import deque
import sys
sys.stdin = open('input', 'r')

def printer_q(arr):
    loc = 0
    global m
    while arr:
        if arr[0] == max(arr):
            arr.popleft()
            loc +=1
            if m==0:
                return loc
            else:
                m-=1

        else:
            arr.append(arr.popleft())
            if m == 0:
                m = len(arr)-1
            else:
                m-=1








T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    arr = [x for x in range(n)]
    q = deque(map(int,input().split()))


    print(printer_q(q))
