n = int(input())
A = list(map(int,input().split()))
P = [0] * n
for i in range(n):
    P[A.index(min(A))] = i
    A[A.index(min(A))] = 10000

print(*P)