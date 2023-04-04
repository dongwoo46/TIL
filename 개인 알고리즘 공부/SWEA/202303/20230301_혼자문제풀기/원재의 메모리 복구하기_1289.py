import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    bit = '3'+input()
    first = [0]*len(bit)
    cnt1 = 0
    cnt = 0
    for i in range(1,len(bit)):
        # 처음에 bit에서 1이 나올 때
        if cnt1 == 0 and bit[i] == '1':
            cnt1 = 1
            cnt += 1

        if cnt1!=0 and bit[i] != bit[i-1]:
            cnt+=1

    print(f'#{tc}', cnt-1)