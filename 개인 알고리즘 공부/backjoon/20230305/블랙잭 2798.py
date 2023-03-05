import sys
sys.stdin = open('input','r')

n,m = list(map(int,input().split()))
numb = list(map(int,input().split()))
ans = 0
max_ans = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans = numb[i]+numb[j]+numb[k]
            if ans<=m:
                max_ans = max(ans,max_ans)

print(max_ans)


