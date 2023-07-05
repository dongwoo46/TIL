import sys
sys.stdin = open('input','r')

input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
lst = data
for i in range(1,n):
    lst[i] = max(lst[i], lst[i]+lst[i-1])

print(max(lst))
# value = 0
# prefix = []
# cnt = 0
#
# for i in data:
#     if i <0:
#         cnt+=1
#     value+=i
#     prefix.append(value)

# max_value = max(prefix)
# if cnt == len(data):
#     print(max(data))
# else:
#     for i in range(n-1,0,-1):
#         for j in range(i-1,-1,-1):
#             if prefix[i] - prefix[j]> max_value:
#                 max_value = prefix[i] - prefix[j]
#
#     print(max(max_value,prefix[0]))

