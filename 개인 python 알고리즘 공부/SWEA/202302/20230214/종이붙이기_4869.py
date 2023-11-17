import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    a = n//10
    paper = [0]*(a+1)
    paper[0] = 0
    paper[1] = 1
    paper[2] = 3
    for i in range(3,a+1):
        paper[i] = paper[i-1] + paper[i-2]*2

    print(f'#{tc} {paper[-1]}')
'''
85 70
181 80
341 90 
725 100
1365 110 
2901 120
5461 130
11605 140 
21845 150 
46421 160 
'''