
import sys
sys.stdin = open('input', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

ans=0
idx=0
cnt=0

while idx!=m-1:
    a= s[idx:idx + 3]
    if s[idx:idx+3] == 'IOI':
        idx +=2
        cnt +=1

        if cnt == n:
            ans+=1
            cnt -= 1
    else:
        idx+=1
        cnt = 0

print(ans)

