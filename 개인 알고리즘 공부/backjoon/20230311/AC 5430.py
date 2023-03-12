import sys
from collections import deque
sys.stdin = open('input','r')


T = int(input())
for tc in range(T):

    order = list(input())
    n = int(input())
    numb = deque(input()[1:-1].split(','))
    if n == 0:
        numb = []
    result = []
    cnt = 0
    for j in order:
        if numb:
            if j == 'R':
                cnt+=1
            elif j == 'D':
                if cnt%2==1:
                    numb.pop()
                else:
                    numb.popleft()

        else:
            if j == 'D':
                print('error')
                break
    else:
        if cnt%2==0:
            print('['+','.join(numb)+']')
        else:
            numb.reverse()
            print('['+','.join(numb)+']')

