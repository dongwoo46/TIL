import sys
sys.stdin = open('input','r')
n, k = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
cnt = 0
for c in coin:
    cnt += k // c
    k = k%c
    if not k:
        break

print(cnt)