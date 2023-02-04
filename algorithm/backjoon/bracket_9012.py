import sys
sys.stdin = open('input','r')


n = int(input())

for i in range(n):
    bracket = input()
    bracket_list = ['(', '{', '[']
    stack = []

    for bk in bracket:
        if bk in bracket_list:
            stack.append(bk)

        if len(stack)!=0:
            if bk == ')' and stack[-1] == '(':
                stack.pop()

            elif bk == '}' and stack[-1] == '{':
                stack.pop()

            elif bk == ']' and stack[-1] == '{':
                stack.pop()

        if len(stack) == 0:
            if bk == ')'or bk =='}' or bk==']':
                print('NO')
                break

    else:
        if len(stack) == 0:
            print('Yes')
        else:
            print('NO')




