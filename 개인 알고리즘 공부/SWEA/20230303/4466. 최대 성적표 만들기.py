import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1,T+1):
    n,k = list(map(int,input().split()))
    score = list(map(int,input().split()))
    result = []
    for i in range(k):
        result.append(max(score))
        score.remove(max(score))

    print(f'#{tc}',sum(result))