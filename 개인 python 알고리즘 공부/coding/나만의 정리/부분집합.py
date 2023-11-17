
# 부분집합 bit뽑기 [1,1,1] ...
def f(i,k):
    if i == k:
        print(bit)
    else:
        # 비트 i = 1일때 탐색
        bit[i] = 1
        f(i+1,k)
        # 비트 i = 0 일때 탐색
        bit[i] = 0
        f(i+1,k)

# 부분집합 원소 뽑기
def f(i, k):
    if i == k:
        for j in range(k):
            if bit[j]:
                print(A[j], end=' ')
    else:
        # 비트 i = 1일때 탐색
        bit[i] = 1
        f(i + 1, k)
        # 비트 i = 0 일때 탐색
        bit[i] = 0
        f(i + 1, k)

# 부분집합의 합 뽑기뽑기
def f(i, k):
    if i == k: # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]
        print(bit, s)
    else:
        # 비트 i = 1일때 탐색
        bit[i] = 1
        f(i + 1, k)
        # 비트 i = 0 일때 탐색
        bit[i] = 0
        f(i + 1, k)


A = [1,2,3]
N = len(A)
bit = [0]*N
f(0,N)