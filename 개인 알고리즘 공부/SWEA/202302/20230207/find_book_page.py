import sys
sys.stdin = open('input', 'r')

T = int(input())

for tc in range(1,T+1):
    page, target_a, target_b = list(map(int,input().split()))
    left = 1
    right = page
    cnt_a = 0
    cnt_b = 0
    middle = int((1+page)/2)
    while middle != target_a:
        middle = int((left+right)/2)
        cnt_a +=1

        if middle> target_a:
            right = middle
        elif middle<target_a:
            left = middle
        else:
            break

    middle = int((1+page)/2)
    left = 1
    right = page
    while middle != target_b:
        middle = int((left+right) / 2)
        cnt_b += 1

        if middle > target_b:
            right = middle
        elif middle < target_b:
            left = middle
        else:
            break

    if cnt_a<cnt_b:
        print(f'#{tc} A')
    elif cnt_a>cnt_b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')

