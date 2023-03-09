import sys
sys.stdin = open('input','r')
x,y,w,h = list(map(int,input().split()))
for i in range(4):
    ans = min(x,y,abs(w-x),abs(h-y))

print(ans)