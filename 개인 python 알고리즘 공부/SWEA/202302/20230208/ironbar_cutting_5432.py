import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    iron = input()
    stack = []
    cnt = 0

    for i in range(len(iron)):
        if iron[i] == '(':
            stack.append(iron[i])
        elif iron[i] ==')':
            if iron[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            elif iron[i-1] == ')':
                stack.pop()
                cnt +=1


    print(f'#{tc} {cnt}')



