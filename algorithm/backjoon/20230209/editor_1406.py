s = input()
str = s + '*'

n = int(input())

for i in range(n):+++++++++++++++++++++++++++++++++++++++++++++++++
    order = input().split()
    print(order)
    idx = str.index('*')
    print(idx)
    if order[0] == 'P':
        str = str[:idx]+order[1]+'*'+str[idx+1:]
    elif order[0] == 'L':
        str = str[:idx-1] + '*' + str[idx-1:]
    elif order[0] == 'D':
        str = str[:idx+1]+'*' + str[idx+1:]
    elif order[0] == 'B':
        str = str[:i-1]+'*'+str[i:]

str_ans = str.replace('*','')
for alpha in str_ans:
    print(alpha, end='')