# 부분집합의 합과 key가 같은 것 뽑기
def f(i, k, key):
    if i == k: # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j] # 부분집합의 합
        if s==key:
            for j in range(k):
                if bit[j]:
                    print(A[j],end=' ')
            print()
    else:
        # 비트 i = 1일때 탐색
        bit[i] = 1
        f(i + 1, k, key)
        # 비트 i = 0 일때 탐색
        bit[i] = 0
        f(i + 1, k, key)

A = [x for x in range(1, 11)]
N = len(A)
key = 10
bit = [0]*N
f(0,N,key)