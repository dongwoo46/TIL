# 백준 파도반 수열 9461

import sys
sys.stdin = open('input', 'r')
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    p = [0] * 101
    p[1] = 1
    p[2] = 1
    p[3] = 1
    p[4] = 2
    for i in range(5,n+1):
        p[i] = p[i-3]+p[i-2]
    print(p[n])