import sys
sys.stdin = open('input', 'r')

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1],x[0]))

# s= 0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i][1] > arr[j][1]:
#             arr[i],arr[j] = arr[j],arr[i]
#     if arr[i][1] == arr[i+1][1]:
#         s = i
#         break
#
# for k in range(s+1,n-1):
#     for l in range(k+1,n):
#         if arr[i][1] > arr[j][1]:
#             arr[i], arr[j] = arr[j], arr[i]
#
for i in arr:
    print(*i)

