a,b,c = list(map(int, input().split()))
# check = list(str(float(a/b)))
#
# idx = 0
# for i in range(len(check)):
#     if check[i] == '.':
#         idx = i
#         break
#
# ans = idx + c
# if len(check) < ans:
#     print(0)
# else:
#     print(check[ans])
for i in range(c):
    a = a%b*10

    ans = (a//b)
print(ans)

