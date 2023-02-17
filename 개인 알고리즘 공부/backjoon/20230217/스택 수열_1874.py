import sys
sys.stdin = open('input','r')

n = int(input())
stack1 = []
stack2 = [i for i in range(n,0,-1)]
result = None
ans = []
for _ in range(n):
    numb = int(input())
    for i in range(numb):
        if stack1:
            if stack1[-1] == numb:
                stack1.pop()
                ans.append('-')
                break
            else:
                if stack2:
                    stack1.append(stack2.pop())
                    ans.append('+')
                else:
                    result = 'NO'
                    break
        else:
            stack1.append(stack2.pop())
            ans.append('+')
        if stack1[-1] == numb:
            stack1.pop()
            ans.append('-')
            break
    if result == 'NO':
        break
else:
    if len(stack1) == 0:
        result = None
    else:
        result = 'NO'


if result:
    print(result)
else:
    for a in ans:
        print(a)

