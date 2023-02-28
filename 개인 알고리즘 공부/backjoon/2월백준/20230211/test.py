def counting_sort(arr, size, m):
    count = [0 for _ in range(m)]
    tmp = [0 for _ in range(size)]

    for x in arr:
        count[x] += 1

    for x in range(1, m):
        count[x] += count[x - 1]

    for x in range(size - 1, -1, -1):
        count[arr[x]] -= 1
        tmp[count[arr[x]]] = arr[x]

    return tmp
print(counting_sort([1 ,9 ,3 ,67 ,2 ,7 ,4 ,25],8,67))

