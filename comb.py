N = 10
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            print(i,j,k)

# n개에서 r개를 고르는 방법(재귀)