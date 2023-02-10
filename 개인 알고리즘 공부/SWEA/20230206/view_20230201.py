'''
건물의 높이가 주어졋을 때  해당 건물을 기준으로
좌 2칸 우2칸 나눴을 때  기준 건물과 양 좌우 2칸에서 제일 큰 값을 뺌
그 해당 건물에서 그 큰 값을 뺏을 때 나오는 개수를  count에 계속 저장

리스트에 해당건물의 좌 1개 2개 우로 1개 2개 의 건물 높이를 리스트에 넣고 거기서 가장 큰값구한다

끝
0~5
'''
import sys
sys.stdin = open("input.txt", "r")
def open_window(arr):
    window = [0,0]
    count = []
    check = []

    for i in range(2,len(arr)-2):
        if arr[i] == max(arr[i - 2:i + 3]):
           window.append(sorted(arr[i-2:i+3],reverse=True)[1])
        else:
            window.append(max(arr[i - 2:i + 3]))


    window.append(0)
    window.append(0)

    for j in range(2,len(arr)-2):
        if arr[j]>window[j]:
            count.append(arr[j]-window[j])
        else:
            continue
    total = sum(count)

    return total



for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = open_window(arr)
    print(f'#{tc} {result}')








