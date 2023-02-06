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

        elif bk == ')':
            if len(stack)!=0:
                if stack[-1] == '(':
                    stack.pop()
            else:
                print('NO')
                break
        elif bk =='}':
            if len(stack)!=0:
                if stack[-1] == '{':
                    stack.pop()
            else:
                print('NO')
                break
        elif bk == ']':
            if len(stack)!=0:
                if stack[-1] == '[':
                    stack.pop()
            else:
                print('NO')
                break

    else:
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')

        # if len(stack)!=0:
        #     if bk == ')' and stack[-1] == '(':
        #         stack.pop()
        #
        #     elif bk == '}' and stack[-1] == '{':
        #         stack.pop()
        #
        #     elif bk == ']' and stack[-1] == '{':
        #         stack.pop()
        #
        # else:
        #     if bk == ')'or bk =='}' or bk==']':
        #         print('NO')
        #         break





