def binarysearch(arr, N, key):
    start = 0
    end = N-1
    while start<=end:
        mid = start + end
        if arr[mid] > key:
            end = mid - 1
        elif arr[mid]<key:
            start = mid + 1
        else:
            return True
    return False
