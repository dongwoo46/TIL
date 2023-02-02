T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    counts = [0] * (max(data) + 1)

    # counts = [1,3,1,1,2]
    for x in data:
        counts[x] += 1

    # 위치를 표현하기 위해서 (자기가 어디에 위치하는지(인덱스표현))
    for i in range(1, len(counts)):
        counts[i] = counts[i] + counts[i - 1]  # counts = [1,4,5,6,8]

    temp = [0] * len(data)

    for num in data[::-1]:
        # counts는 첫번째 인덱스가 1이기때문에 counts[num]-1을 하는거
        temp[counts[num] - 1] = num
        counts[num] -= 1

    # print(f'#{tc} {temp}')

    print('#%d' % tc, *temp)