
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

##리스트 슬라이싱 문제풀이
import sys
sys.stdin = open('input', 'r')

s = input()
str = s + '*'

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    order = sys.stdin.readline().split()
    idx = str.index('*')
    if order[0] == 'P':

        if str[-1] == '*':
            str = str[:idx] + order[1] + '*'
        elif idx == 0:
            str = order[1] + '*' + str[idx+1:]
        else:
            str = str[:idx]+order[1]+'*'+str[idx+1:]
    elif order[0] == 'L':
        if idx == 0:
            continue
        elif str[-1] == '*':
            str = str[:idx-1]+'*'+str[-2]
        else:
            str = str[:idx-1] + '*' + str[idx-1]+str[idx+1:]
    elif order[0] == 'D':
        if str[-1] == '*':
            continue
        elif idx == 0:
            str = str[:idx+1] + '*' + str[idx+2:]
        else:
            str = str[:idx]+str[idx+1]+'*'+ str[idx+2:]
    else:
        if idx == 0:
            continue
        elif str[-1] == '*':
            str = str[:idx-1]+'*'
        else:
            str = str[:idx-1]+'*'+str[idx+1:]


str_ans = str.replace('*','')
for alpha in str_ans:
    print(alpha, end='')