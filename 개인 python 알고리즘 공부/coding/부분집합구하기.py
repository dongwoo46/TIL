
def f(start,k):
    if k == 5:   #하나의 부분집합 완성
        for j in range(5):
            if bit[j]:
                print(A[j], end=' ')
        print()


    for i in range(start, len(A)):
        bit[i] = 1
        f(i+1,k+1)
        bit[i] = 0
        f(i+1,k+1)
A = [1,2,3,4,5,6,7,8,9]
# key = 10
bit = [0]*len(A)
f(0,0)