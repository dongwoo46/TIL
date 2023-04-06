import sys
sys.stdin = open('input','r')
n,m = map(int,input().split())
s = set()
for i in range(n):
    s.add(input())
cnt = 0
for i in range(m):
    word = input()
    if word in s:
        cnt+=1
print(cnt)