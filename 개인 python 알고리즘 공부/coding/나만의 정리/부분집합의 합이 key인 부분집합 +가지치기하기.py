# # 부분집합의 합이 key인 부분집합의 개수 뽑기
# def f(i, k, s, t): # i 원소 , k집합의크기 , s i-1까지 고려된 합, t 찾고자하는ㄴ목표
#     global cnt
#     if s> t: #고려한 원소의 합이 찾는 합보다 큰경우 종료
#         return
#     elif s == t: # 남은 원소를 더이상 고려할 필요 없음 이미 목표에 도달
#         cnt+=1
#         return
#     elif i == k: # 하나의 부분집합 완성
#         return
#
#     else:
#         f(i+1,k,s+A[i],t) #A[i]포함
#         f(i+1,k,s,t) # A[i] 미포함
#
A = [x for x in range(1, 11)]
N = len(A)
key = 10
cnt = 0
bit = [0]*N

# print(cnt) # 부분집합의 합의 key인 수가 몇개인가


####
# 부분집합의 합이 key인 부분집합의 개수 뽑기
def f(i, k, s, t): # i 원소 , k집합의크기 , s i-1까지 고려된 합, t 찾고자하는ㄴ목표
    global cnt
    if i == k: # 하나의 부분집합 완성
        if s==t:
            for j in range(k): # 특정원소가 포함된
                if bit[j]:
                    print(A[j], end=' ')
            print()
            cnt += 1
        return

    else:
        bit[i] = 1
        f(i+1,k,s+A[i],t) #A[i]포함
        bit[i] = 0
        f(i+1,k,s,t) # A[i] 미포함


f(0,N,0,key)
# print(cnt) # 부분집합의 합의 key인 수가 몇개인가