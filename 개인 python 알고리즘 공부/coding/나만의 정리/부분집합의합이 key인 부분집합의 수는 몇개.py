# 부분집합의 합이 key인 부분집합의 개수 뽑기
def f(i, k, s, t): # i 원소 , k집합의크기 , s i-1까지 고려된 합, t 찾고자하는ㄴ목표
    global cnt
    if i == k: # 하나의 부분집합 완성
        if s==t:
            cnt += 1
        return

    else:
        f(i+1,k,s+A[i],t) #A[i]포함
        f(i+1,k,s,t) # A[i] 미포함

A = [x for x in range(1, 11)]
N = len(A)
key = 10
cnt = 0
bit = [0]*N
f(0,N,0,key)
print(cnt) # 부분집합의 합의 key인 수가 몇개인가


####
# 부분집합의 합이 key인 부분집합 뽑기
def f(i, k, s, t): # i 원소 , k집합의크기 , s i-1까지 고려된 합, t 찾고자하는ㄴ목표
    global cnt
    if i == k: # 하나의 부분집합 완성
        if s==t:
            for j in range(k):
                if bit[j]:
                    print(A[j], end=' ')
            cnt += 1
        return

    else:
        bit[i] = 1
        f(i+1,k,s+A[i],t) #A[i]포함
        bit[i] = 0
        f(i+1,k,s,t) # A[i] 미포함



print(cnt) # 부분집합의 합의 key인 수가 몇개인가