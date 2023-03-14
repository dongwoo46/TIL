import sys
sys.stdin = open('input','r')
T = int(input())
for tc in range(1,T+1):
    s,e = map(int,input().split())
    d = e-s
    k = [0]*(d+1)
    k[1] = 1
    numb = 2
    result = 2
    loc = 2
    while True:
        if k[-1]:
            break
        for i in range(numb-1):
            k[loc] = result
            loc +=1
            if k[-1]:
                break
        result+=1
        numb+=1
    print(k[d])
