arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 널리 사용되고 있는 가장 직관적 형태의 퀵정렬 소스코드
def quick_sort(arr, start, end):
    if start>=end: # 원소가 1개이면 종료
        return
    pivot = start # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while left<=right:
        # 오른쪽에서부터 왼쪽으로 피벗보다 큰 데이터를 찾을때 까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 왼쪽에서부터 오른족으로 피벗보다 작은 데이터를 찾을때 까지 반복
        while right>start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은데이터와 피벗을 교체
            arr[right],arr[pivot] = arr[pivot],arr[right]
        else:
            arr[left],arr[right] = arr[right],arr[left]
    # 분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(arr,start,right-1)
    quick_sort(arr, right+1, end)

quick_sort(arr,0,len(arr)-1)
print(arr)

# 파이썬 장점을 살린 퀵 정렬 소스코드
def quick_sort(arr):
    # 리스트가 하나 이하의 원소만 가지고 있으면 종료
    if len(arr)<=1:
        return arr
    pivot = arr[0] # 피벗은 arr의 첫번재 원소
    tail = arr[1:0] # 피벗을 제외한 arr리스트

    left_side = [x for x in tail if x<=pivot] #분할된 왼쪽부분
    right_side = [x for x in tail if x>pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] +quick_sort(right_side)
print(quick_sort(arr))