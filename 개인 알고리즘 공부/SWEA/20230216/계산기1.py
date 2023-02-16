import sys
sys.stdin = open('input','r')
for tc in range(1,11):
    n = int(input())
    calculation = input()
    stack = []
    for cal in calculation:
        if cal.isdigit():
            stack.append(int(cal))
            if len(stack)==2:
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
    if stack:
        print(f'#{tc}',stack.pop())



