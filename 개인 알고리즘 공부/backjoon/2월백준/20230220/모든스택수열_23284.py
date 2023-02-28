n = int(input())

def f(i,k):
    if i == k:
        #하나의 부분집합 완성
        for j in range(k):
            if bit[j]:
                ans.append(A[j])
        if len(ans) == k:
            result.append(ans)
    else:
        bit[i] = 1
        f(i+1,k+1)
        bit[i] = 0
        f(i+1,k+1)

A = [x for x in range(1,n+1)]
bit = [0] * n
ans = []
result = []
f(0,0)
print(*result)