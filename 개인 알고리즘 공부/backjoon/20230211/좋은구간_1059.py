import sys
sys.stdin = open('input','r')


n = int(input())
numb_list = list(map(int, input().split()))
target = int(input())

for i in range(len(numb_list)):
    if target == numb_list[i]:
        print(0)
        break
    else:
        numb_list.append(target)
        numb_list.sort()
        idx = numb_list.index(target)
        a,x,b = idx-1,idx,idx+1
        if
L = int(input())
nums = list(map(int, input().split()))
target = int(input()) # == n

nums.append(0)
nums.sort()

A = 0
for i in range(len(nums)-1) :
    if nums[i] == target or nums[i+1] == target:
        A = 0
        break
    elif nums[i] < target and target < nums[i+1]:
        A = (target - nums[i]) * (nums[i+1] - target) - 1
        break

print(A)
# numb_list1 = numb_list
# numb_list1.append(target)
#
# numb_list1.sort()
# idx = numb_list1.index(target)
#
# a,x,b = idx-1,idx,idx+1
#
# if target == numb_list1[a] or target == numb_list1[b] or :
#     print(0)
# else:
#     if x !=0 :
#         if (numb_list1[x]-numb_list1[a])*(numb_list1[b]-numb_list1[x])-1 <=0:
#             print(0)
#         else:
#             print((numb_list1[x]-numb_list1[a])*(numb_list1[b]-numb_list1[x])-1)
#     elif x ==0:
#         if (numb_list1[b]-numb_list1[x]-1) <=0:
#             print(0)
#         else:
#             print(numb_list[b]-numb_list[x]-1)
