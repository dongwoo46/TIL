# for i in range(4):
#     if x & (1<<object):
#         res += '1'
#     else:
#         res += '0'
import sys
sys.stdin = open('input', 'r')

T = int(input())

for tc in range(1,T+1):
    length, numb = input().split()
    ans = ''
    n = 0
    mult = 0
    ten = int(numb, 16)
    two = bin(ten)[2:]
    if len(two)%4 !=0:
        while True:
            if 4*n<len(two)<4*(n+1):
                mult = n+1
                break
            n+=1

    print(f'#{tc}', '0'*(4*(mult)-len(two))+two)

