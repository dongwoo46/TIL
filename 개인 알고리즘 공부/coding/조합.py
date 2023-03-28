N = 10
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            print(i,j,k)

def nCr(n,r,s): # n개에서 r개를 고르는 조합, s 고를 수 있는 구간의 시작 인덱스
    if r==0:
        print(comb)
    else:
        for i in range(s,n-r+1):
            comb[r-1] = A[i]
            nCr(n,r-1,i+1)

n = 5
r = 3
comb = [0]*3
A = [x for x in range(x)]