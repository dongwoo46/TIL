# SWEA baby gin game
import sys
sys.stdin = open('../../../input', 'r')

def backtracking(v,s):
    global ans
    if v == 6:
        if triplet(s)+runn(s)>=2:
            ans = 'True'
        return
    else:
        for i in range(6):
            if not visited[i]:
                visited[i] = 1
                backtracking(v+1,str(arr[i])+s)
                visited[i] = 0

def  triplet(arr):
    trip = 0
    if arr[0] == arr[1] == arr[2]:
        trip +=1
    if arr[3] == arr[4] == arr[5]:
        trip += 1
    return trip

def runn(arr):
    cnt =0
    if int(arr[0])+1 == int(arr[1]) and int(arr[1])+1 == int(arr[2]):
        cnt+=1
    if int(arr[3])+1 == int(arr[4]) and int(arr[4])+1 == int(arr[5]):
        cnt += 1
    return cnt



T = int(input())
for tc in range(1,T+1):
    arr = list(map(int,input()))
    visited = [0] * 6
    ans = 'False'
    backtracking(0,'')
    print(ans)


# def perm(i,k):
#     if i== k:
#         print(*p)
#     else:
#         for j in range(k): # 사용하지 않는 숫자를
#             if used[j] == 0: # used에서 순서대로 검색
#                 p[i] = A[j]
#                 used[j] = 1 # j번째 숫자 사용으로 표시
#                 perm(i+1,k)
#                 used[j] = 0 # j번 자리 숫자를 다른 자리에서 쓸 수 있게
#
# A = [1,4,5]
# p = [0]*3
# k =3
# used = [0]*3
# perm(0,3)