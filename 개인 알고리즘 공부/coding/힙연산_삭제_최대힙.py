def deq():
    global last
    tmp = heap[1]          #루트 임시저장
    heap[1] = heap[last]   #마지막 정점의 값을 루트로 이동
    last -= 1              # 마지막 정점 삭제
    p = 1
    c = p*2                # 왼쪽 자식 번호
    while c <= last:       # 자식이 하나 이상 있으면
        if c+1 <= last and heap[c] < heap[c+1]:  # 오른쪽 자식도 있고 오른쪽 자식의 키가 더 크면
            c += 1          # 비교대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]: # 자식이 부모보다 더 크면 (최대힙)
            heap[c], heap[p] = heap[p], heap[c]
            p = c
            c = p*2
        else:
            break
    return tmp

def enq(n):
    global last
    last += 1       #완전 이진 트리에 마지막 정점을 추가
    heap[last] = n  #마지막 정점에 저장
    c = last        #부모가 있고,부모>자식 조건 검사를 위해
    p = c//2
    while p>0 and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 옮긴자리에서 부모와 비교하기 위해
        p = c//2
    return

heap = [0] * 101  # 완전 이진 트리 1번~100번 인덱스 준비
last = 0  # 완전 이진트리의 마지막 정점 번호
enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

while last>0:
    print(deq())