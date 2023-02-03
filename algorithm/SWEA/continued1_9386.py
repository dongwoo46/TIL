import sys
sys.stdin = open("input", "r")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    numbers = input()
    cnt = 0
    cnt_list = []

    for i in range(len(numbers)):
        if numbers[i] == '1':
            cnt +=1
            if i == len(numbers)-1:
                cnt_list.append(cnt)
                break
        else:
            cnt_list.append(cnt)
            cnt = 0

    print(f'#{tc} {max(cnt_list)}')





