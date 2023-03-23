import sys
sys.stdin = open('input.txt','r')
n, m = map(int,input().split())
arr = [0]+list(map(int,input().split()))+[0]
for i in range(m):
    s, e = map(int,input().split())
    total = 0
    for j in range(s,e+1):
        total += arr[j]
    print(total)