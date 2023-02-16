
def f(i,k, key):
    if i == k:   #하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s += A[j]  # 부분집합의합
                print(A[j], end=' ')
        # if s == key:
        #     return 1
        # else:
        #     return 0
        # if s == key:    #합이 key와 같은 부분집합 출력
        #     for j in range(k):
        #         if bit[j]:
        #             print(A[j], end='')
        # print()
        print(bit,s)

    else:
        bit[i] = 1
        f(i+1,k,key)
        bit[i] = 0
        f(i+1,k,key)
A = [1,2,3]
key = 10
bit = [0]*len(A)
f(0,3,10)