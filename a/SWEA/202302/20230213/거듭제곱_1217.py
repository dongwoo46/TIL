import sys
sys.stdin = open('input', 'r')
for tc in range(1,11):
    t = int(input())
    n,m = list(map(int,input().split()))
    numb = n**m
    print(f'#{t} {numb}')