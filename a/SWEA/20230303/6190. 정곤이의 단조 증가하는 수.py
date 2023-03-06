import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    increase = list(map(int,input().split()))
    check = []
    check2 = []
    max_numb = -1
    inc_numb = -1

    # Ai*Aj 인 check 리스트 만듦
    for i in range(n-1):
        for j in range(i+1,n):
            check.append(increase[i]*increase[j])
    # check리스트를 돌면서 확인
    for numb in check:
        # check리스트의 값들을 자릿수 크기를 구별하기 위해 str로 나눠줌
        check2 = list(map(int,str(numb)))
        # check2가 1일때는 그냥 바로 비교
        if len(check2) == 1:
            max_numb = max(max_numb,int(numb))
        else:
            # 1이 아니라면 for문으로 check2의 왼쪽값이 오른쪽값보다 크다면 반복 종료
            for k in range(len(check2)-1):
                if int(check2[k])>int(check2[k+1]):
                    break
            # 만약 반복종료하지 않고 다 돈다면 inc_numb을 int(numb)으로 갱신
            else:
                inc_numb = int(numb)
        #max_numb과 inc_numb중 최대값 고름
        max_numb = max(max_numb,inc_numb)

    print(f'#{tc}', max_numb)


