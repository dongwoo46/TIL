# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

import sys
from collections import deque
sys.stdin = open('input', 'r')

dslr = ['D','S','L','R']

def bfs(a,b):
    q= deque()
    q.append((a,''))
    while q:
        t = q.popleft()
        for i in  dslr:
            if i == 'D':
                x = int(t)*2
                if x>9999:
                    x=x%10000
                q.append(str(x))
                if x == b:
                    return ans
            elif i =='S':
                if int(t) == 0:
                    x = 9999
                else:
                    x = int(t)-1
                q.append(str(x))
                ans+=i
                if x == b:
                    return ans
            elif i == 'L':
                x = t[1:4]+t[0]
                ans += i
                q.append(x)
                if x == b:
                    return ans
            elif i == 'R':
                x = t[-1]+t[0:3]
                ans += i
                q.append(x)
                if x == b:
                    return ans


n= int(input())
for i in range(n):
    a,b = input().split()
    print(bfs(a,b))