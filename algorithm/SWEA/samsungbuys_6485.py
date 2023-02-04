import sys
sys.stdin = open("input", "r")

T = int(input())


for tc in range(1,T+1):
    N = int(input())
    cnt_list = [0] * 5100
    for _ in range(N):
        a, b = list(map(int, input().split()))

        for i in range(a,b+1):
            cnt_list[i] +=1

    P = int(input())
    ans_list =[]
    for _ in range(P):
        c = int(input())
        ans_list.append(cnt_list[c])



    print(f'#{tc}',*ans_list)






