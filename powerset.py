# powerset 만들기

cnt = 1

def process_solution(arr, k, res):
    global cnt
    if res != 10:
        return

    print(f'{cnt} :', end='')
    cnt += 1
    for i in range(k):
        if arr[i]:
            print(lst[i], end=' ')
    print()


def powerset(arr, k, n, res):
    global cnt
    c = [1, 0]
    ncands = 2

    if res > 10:  # 유망하지 않으면 진행 x
        return

    if k == n:
        process_solution(arr, k, res)
    else:
        for i in range(ncands):
            arr[k] = c[i]
            if arr[k]:  # k번째 선택
                powerset(arr, k+1, n, res + lst[k])
            else:  # k번째 선택 안함
                powerset(arr, k+1, n, res)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
arr = [0] * N  # arr[i]를 포함시키는 경우 1
powerset(arr, 0, N, 0)