import sys
sys.stdin = open('input', 'r')

def fibonacci(n):
    global cnt1
    global cnt0
    if n == 0:
        cnt0+=1
        return 0
    elif n == 1:
        cnt1+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cnt0 = [0]*41
    cnt1 = [0]*41
    cnt0[0] = 1
    cnt1[0] = 0
    cnt0[1] = 0
    cnt1[1] = 1

    for j in range(2, n+1):
        cnt0[j] = cnt0[j-1] + cnt0[j-2]
        cnt1[j] = cnt1[j - 1] + cnt1[j - 2]

    print(cnt0[n], cnt1[n])
