#SWEA 수영장

import sys
sys.stdin = open('../../../../input')

def backtracking(v,total):
    global mn
    if v>=12:
        mn = min(mn,total)
        return
    backtracking(v+1,total+use[v]*d)
    backtracking(v + 1, total + m)
    backtracking(v + 3, total + t)
    backtracking(v + 12, total + y)



T = int(input())
for tc in range(1,T+1):
    d,m,t,y = map(int,input().split())
    use = list(map(int,input().split())) # 1일  # 1달 # 3달 # 1년
    mn = 1e9
    backtracking(0,0)
    print(f'#{tc}', mn)