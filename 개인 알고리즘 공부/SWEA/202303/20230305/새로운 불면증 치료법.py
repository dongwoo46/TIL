import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    n= int(input())

    ten = []
    cnt=0

    while True:
        if len(set(ten)) == 10:
            break
        cnt += 1
        numb = list(map(int,str(n*cnt)))
        for i in numb:
            ten.append(i)


    print(f'#{tc}',cnt*n)

