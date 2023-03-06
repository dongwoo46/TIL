import sys
sys.stdin = open('input','r')
T= int(input())
for tc in range(1,T+1):
    n = int(input())
    ans = -1
    min_ans = 10000000000000
    carrot = list(map(int,input().split()))
    carrot.sort()
    for i in range(n-2):
        for j in range(i+1,n-1):
            if carrot[i]!=carrot[i+1] and carrot[j] != carrot[j+1]:
                box1 = i+1
                box2 = j-i
                box3 = n-1-j
                if box1*box2*box3 != 0 and box1<=n//2 and box2<=n//2 and box3<=n//2:
                    ans = max(box1,box2,box3)-min(box1,box2,box3)
                    min_ans = min(min_ans,ans)
    else:
        if ans == -1:
            min_ans = ans




    print(f'#{tc}', min_ans)
