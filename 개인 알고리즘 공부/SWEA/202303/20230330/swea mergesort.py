import sys
sys.stdin = open('input')

#병합정렬

def merge(left, right):
    i, j = 0, 0
    result = []
    global cnt
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[-1] > right[-1]:
        cnt += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def merge_sort(m):
    if len(m) <= 1: # 크기가 1이하면 반환
        return m

    # 리스트 left right로 나누기
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    # 새롭게 만들어진 리스트 각각 병합
    new_left = merge_sort(left)
    new_right = merge_sort(right)
    return merge(new_left,new_right)

T = int(input())
for tc in range(1,T+1):
    n =int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    result = merge_sort(arr)
    print(f'#{tc}',result[n//2], cnt)