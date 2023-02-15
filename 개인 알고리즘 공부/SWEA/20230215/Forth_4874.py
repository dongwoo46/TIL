import sys
sys.stdin = open('input','r')

# import ast

operator = ['+','-','/','*']


# def change_operator(str):
#     if str == '+':
#         return +
#     elif str == '-':
#         return -

T = int(input())
for tc in range(1,T+1):
    stack = []
    ans = ''
    calculation = input().split()
    for cal in calculation:
        if cal == '.':
            if len(stack) == 1:
               ans.append(stack.pop())
            else:
                ans.append('error')

        elif cal in operator:
            if len(stack)== 0 or len(stack) == 1:
                ans.append('error')
                break

            else:
                b = stack.pop()
                a = stack.pop()
                if cal == '+':
                    compute = a + b
                elif cal == '-':
                    compute = a-b
                elif cal == '/':
                    compute = int(a/b)
                elif cal == '*':
                    compute = a*b
                stack.append(compute)
        else:
            stack.append(int(cal))

    print(f'#{tc} {ans[0]}')


'''
2.
expression = a+cal+b
parsed_expression = ast.parse(expression, mode='eval')
compiled_expression = compile(parsed_expression, filename='<string>', mode='eval')
result = eval(compiled_expression)
compute = str(result)
'''
# 1. compute = str(eval(a+cal+b))







