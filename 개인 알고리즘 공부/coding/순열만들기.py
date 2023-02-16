# def f(i,k):
#     if i ==k:
#         print(p)
#     else:
#         for j in range(k):
#             p[i], p[j] = p[j], p[i]
#             # p[i]결정 , p[i]와 관련된 작업 가능
#             f(i+1,k)
#             p[i], p[j] = p[j],p[i]
#
# input = 전체 원소수
# k = 현재 i번째까지 선택

def f(i,k):
    if i == k:
        print(bit)
    else:
        bit[i] = 1
        f(i+1,k)
        bit[i] = 0
        f(i+1,k)



A = [1,2,3]
N = len(A)
bit = [0]*N
f(0,N)