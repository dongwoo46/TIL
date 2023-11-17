def f(i,k,s,t): #i원소, k 집합의 크기 , s i-1까지의 고려된 합, t 찾고자 하는 목표(합)
    global cnt
    global fcnt #함수 호출횟수 카운트
    fcnt += 1
    if s>t: #고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s ==t : #남은 원소를 고려할 필요ㅏ 없는 경우
        cnt +=1
        return

    if i ==k:
        if s == t:
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j],end=' ')
            # print()
            cnt +=1

        return
    else:
        bit[i] = 1
        f(i+1,k,s+A[i],t) #A[i]포함
        bit[i] = 1
        f(i+1, k, s, t) #A[i] 미포함








cnt = 0
A = [1,2,3,4,5,6,7,8,9,10]
N = len(A)
key = 10
fcnt = 0
bit = [0]*len(A)

f(0,N,0,key)
print(cnt)
print(fcnt)