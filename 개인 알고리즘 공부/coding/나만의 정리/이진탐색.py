# 재귀함수로 구현한 이진탐색
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) //2
    # 찾은 경우 중간점 인덱스 반환
    if arr[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은경우
    elif arr[mid] > target:
        return binary_search(arr,target,start,mid-1)
    else:
        return binary_search(arr, target,mid+1,end)

# 반복문으로 구현한 이진 탐색 코드
def binary_search(arr,target,start,end):
    while start<=end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return

