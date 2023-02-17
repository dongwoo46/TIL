def binary(arr ,n ,key):
    start = 0
    end = n -1
    while start<=end:
        mid = (start+end)//2
        if arr[mid]> key:
            end = mid-1
        elif arr[mid]<key:
            start = mid +1
        else:
            return True

n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
m = int(input())
list2 = list(map(int,input().split()))

for i in list2:
    if binary(list1,len(list1),i):
        print(1)
    else:
        print(0)
