import math
while True:
    arr = list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        long = max(arr)
        arr.remove(long)

        if long**2 == arr[0]**2+arr[1]**2:
            print('right')
        else:
            print('wrong')