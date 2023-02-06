def open_window(arr):
    window = [0,0]
    count = []

    for i in range(2,len(arr)-2):
        if arr[i] == max(arr[i - 2:i + 3]):
            window.append(sorted(arr[i-2:i+3],reverse=True)[1])
        else:
            window.append(max(arr[i - 2:i + 3]))

    window.append(0)
    window.append(0)

    for j in range(2,len(arr)-2):
        if arr[j]>window[j]:
            count.append(arr[j]-window[j])
        else:
            continue
    total = sum(count)

    return total


for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = open_window(arr)
    print(f'#{tc} {result}')