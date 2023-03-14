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