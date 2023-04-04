import sys
sys.stdin = open('input')

# 퀵정렬

def quick_sort(arr):
    # 리스트가 하나 이하의 원소만 가지고 있으면 종료
    if len(arr)<=1:
        return arr
    pivot = arr[0] # 피벗은 arr의 첫번재 원소
    lst = arr[1:] # 피벗을 제외한 arr리스트

    left_side = [x for x in lst if x<=pivot] #분할된 왼쪽부분
    right_side = [x for x in lst if x>pivot] #분할된 오른쪽 부분

    #분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
    return quick_sort(left_side) + [pivot] +quick_sort(right_side)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc}',quick_sort(arr)[n//2])