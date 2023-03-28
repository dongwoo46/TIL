import sys
sys.stdin = open('../../../input')

def triplet(count):
    if max(count)==3:
        return True


def runcheck(count):
    for i in range(8):
        if count[i]>=1 and count[i+1]>=1 and count[i+2]>=1:
            return True


T =int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    p1 = []
    p2 = []
    count1 = [0]*10
    count2 = [0]*10
    w1 = 0
    w2 = 0
    ans = -1
    winner = 0
    for i in range(12):
        if i%2 == 0:
            p1.append(arr[i])
            count1[arr[i]]+=1
        else:
            p2.append(arr[i])
            count2[arr[i]]+=1
        if triplet(count1):
            w1 = 1
        if runcheck(count1):
            w1 = 1
        if triplet(count2):
            w2 = 1
        if runcheck(count2):
            w2 = 1
        if w1 == 1 and w2 != 1:
            ans = 1
        elif w2 == 1 and w1!=1:
            ans = 2
        elif w1 == 1 and w2==1:
            ans = 0

        if ans != -1:
            break
    if ans == -1:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', ans)
