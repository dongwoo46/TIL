import sys
str1 = list(input())
str2 = []


n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()
    if order[0] == 'P':
        str1.append(order[1])
    elif order[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif order[0] == 'D':
        if str2:
            str1.append(str2.pop())
    else:
        if len(str1) !=0:
            str1.pop()
str1.extend(reversed(str2))
print(''.join(str1))