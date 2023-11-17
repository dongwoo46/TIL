'''
최대 힙 구현
100개의 숫자가 들어올 수 있다  heap = [0] * 101
last = 0 #마지막 정점 번호

#완전 이진트리 1차원배열 만들고
#0번 인덱스 사용 x
#마지막 last까지
last = 0
enq(n)
    last += 1 #마지막 정점 추가
    heap[last]= n
    c = last # 부모>자식 확인을 위해
    p = c//2
    while p>0 and heap[p] >heap[c]: #부모가 있으면서 부모가 값이 더 작다면
        heap[c],heap[p] = heap[p], heap[c] #부모기 있는데 부모가 자식들보다 작으면 교환
        c = p
        p = c//2
        # 재귀는 오른쪽으로가다가 왼쪽으로갈까?? 고민할때 사용 하면좋음
'''

#최대 100개의 key
#최대 힙
def enq(n):
    global last
    last += 1       #완전 이진 트리에 마지막 정점을 추가
    heap[last] = n  #마지막 정점에 저장
    c = last        #부모가 있고,부모>자식 조건 검사를 위해
    p = c//2
    while p>0 and heap[p] > heap[c]: #부모가 있으면서 부모가 값이 더 크다면
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 옮긴자리에서 부모와 비교하기 위해
        p = c//2
    return

heap = [0] * 101    #완전 이진 트리 1번~100번 인덱스 준비
last = 0            # 완전 이진트리의 마지막 정점 번호
enq(7)
print(heap[1])

enq(2)
print(heap[1])
enq(5)
print(heap[1])

enq(3)
print(heap[1])
enq(4)
enq(6)
print(heap)

