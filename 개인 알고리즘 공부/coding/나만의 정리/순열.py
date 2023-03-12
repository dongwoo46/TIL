# 단 사전순으로 안 나옴 , 또한 p만 출력하는거라서
# p의 길이보다 작은 부분집합을 구할 때는 사용 X
def f(i,k):
    if i == k:
        print(p)
    else:
        for j in range(i, k):
            p[i],p[j] = p[j],p[i]
            f(i+1,k)
            p[i], p[j] = p[j], p[i]

p = [1,2,3]
N = len(p)
f(0, N)