arr = list(map(int,input().split()))
for i in range(1,1<<len(arr)):
    total = 0
    result = []
    for j in range(len(arr)):
        if i & (1<<j): # 1의 j번째 위치가 1이라면
            total += arr[j] # j번째 원소를 부분집합에 포함
            result.append(arr[j])

    if total == 0:
        print(*result)
