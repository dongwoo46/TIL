import sys
sys.stdin = open("input", "r")

T = int(input())
for tc in range(1,T+1):
    N, K = list(map(int, input().split()))
    A = [x for x in range(1, 13)]
    cnt = 0
    ans_set = []

    for i in range(1<<12):
        sub_set = []
        for j in range(12):
            if i & (1<<j):
                sub_set.append(A[j])
        ans_set.append(sub_set)

    for i in ans_set:
        if len(i) == N and sum(i) == K:
            cnt+=1

    print(f'#{tc} {cnt}')
