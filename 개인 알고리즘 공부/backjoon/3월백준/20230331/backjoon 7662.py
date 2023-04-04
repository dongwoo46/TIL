# 백준 이중우선순위큐
import heapq
import sys
sys.stdin = open('../../../../input')
input = sys.stdin.readline
mx = 0
mn = 1e9
T = int(input())

for tc in range(1,T+1):
    n = int(input())
    h = []  # 최소힙
    h_max = []  # 최대힙
    flag = 0
    for i in range(n):
        order, numb = input().split()
        numb = int(numb)
        if order == "I": # heapq에 숫자 인풋하기
            heapq.heappush(h, numb)
            heapq.heappush(h_max, (-numb,i))
        else:
            if len(h) !=0:
                if order == "D" and numb==1:# heapq에서 최소 값 뽑아내기
                    heapq.heappop(h)

                elif order == "D" and numb== -1: #heapq에서 최대값 뽑아내기
                    h = h[:len(h)-1]

            else:
                if order=="D":
                    ans = 'EMPTY'
                    flag = 1

    if flag == 0:
        print(max(h),min(h))
    else:
        print("EMPTY")