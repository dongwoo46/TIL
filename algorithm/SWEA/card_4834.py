# import sys
# sys.stdin = open("input", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    counts = [0] * 10
    list1 = []

    for numb in arr:
        counts[numb] += 1

    for i in range(10):
        if max(counts) == counts[i]:
            ans = i
    print(f'#{tc} {ans} {max(counts)}')