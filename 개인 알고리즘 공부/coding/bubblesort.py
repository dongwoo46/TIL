arr = [1,2,3,4,5,6]

for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

'''
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
'''