n = list(map(int, input().split()))
# ans = ''
# for i in range(1,9):
#     if i == n[i-1]:
#         ans = 'ascending'
#     elif 9-i == n[i-1]:
#         ans = 'descending'
#     else:
#         ans = 'mixed'
#         break
#
# print(ans)

list1 = [1,2,3,4,5,6,7,8]
list2 = [8,7,6,5,4,3,2,1]
if n == list1:
    print('ascending')
elif n == list2:
    print('descending')
else:
    print('mixed')