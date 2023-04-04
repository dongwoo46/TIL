# 백준 이중우선순위큐
import sys
sys.stdin = open('input')
import heapq
input = sys.stdin.readline

mx = 0
mn = 1e9
T = int(input())
for tc in range(1,T+1):
    n = int(input())
    h = []  # 최소힙
    h_max = []  # 최대힙
    visited = [0] * 1000001
    for i in range(n):
        order, numb = input().split()
        numb = int(numb)

        if order == "I": # heapq에 숫자 인풋하기
            heapq.heappush(h, (numb,i))
            heapq.heappush(h_max, (-numb,i))
            visited[i] = True  # 힙에 값이 들어있음
        elif order =="D": # 삭제시 key를 통해 다른힙에서 삭제된 것인지 확인
            if numb == -1: # 다른힙에 의해 삭제된 노드라면 삭제되지 않은 노드가 나올때까지 버림 삭제노드가 나오면 노드삭제
                while h and not visited[h[0][1]]: # visited가 0이면 노드가 삭제됨
                    heapq.heappop(h) # 버리기
                if h:
                    visited[h[0][1]] = 0
                    heapq.heappop(h)
            elif numb == 1:
                while h_max and not visited[h_max[0][1]]:
                    heapq.heappop(h_max)
                if h_max:
                    visited[h_max[0][1]] = 0
                    heapq.heappop(h_max)

        # 연산이 끝난 후에도 필요없는 노드가 있을 수 있으니 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값 출력
        while h and not visited[h[0][1]]:
            heapq.heappop(h)
        while h_max and not visited[h_max[0][1]]:
            heapq.heappop(h_max)

    if h and h_max:
        print(-h_max[0][0], h[0][0])
    else:
        print('EMPTY')

