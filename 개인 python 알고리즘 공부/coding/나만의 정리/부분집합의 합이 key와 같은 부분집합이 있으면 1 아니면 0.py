# 부분집합의 합 뽑기뽑기
def f(i, k, key):
    if i == k: # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        if s == key:
            return 1
        else:
            return 0
    else:   # 비트 i = 1일때 탐색
        bit[i] = 1
        if f(i + 1, k, key):
            return 1
        # 비트 i = 0 일때 탐색
        bit[i] = 0
        if f(i + 1, k, key):
            return 1
        return 0

A = [x for x in range(1, 11)]
N = len(A)
key = 10
bit = [0]*N
print(f(0,N,key))