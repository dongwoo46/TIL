n = bin(int(input()))[2:]
ans = 0

for i in range(len(n)):
    if n[i] == '1':
        ans += 3**(len(n)-i-1)
print(ans)


# n = int(input())
# numb_list = [3**i for i in range(n)]
# ans_list = []
#
# for i in range(n):
#     ans_list.append(3**i)
#     if ans_list[len(ans_list)-1] != 3**i:
#         ans_list.append(ans_list[i]+3**i)
#     else:
#         continue
# print(ans_list[n-1])

# for i in range(n):
#     ans_list.append(numb_list[i])
#
#     for j in range(len(ans_list)):
#         if numb_list[i] != ans_list[j]:
#             ans_list.append(numb_list[i] +ans_list[j])
#         else:
#             continue
#


