cry = list(input())
cnt=0
stack1 = []
for a in cry:
    if a == 'q':
        stack1.append(a)
    elif 'q' in stack1 and  a == 'u':
        stack1.append(a)
        stack1.remove('q')
    elif 'u' in stack1 and a == 'a':
        stack1.append(a)
        stack1.remove('u')
    elif 'a' in stack1 and a == 'c':
        stack1.append(a)
        stack1.remove('a')
    elif 'c' in stack1 and a == 'k':
        stack1.append(a)
        stack1.remove('c')
        stack1.pop()
        cnt += 1
    # elif len(stack1) !=0:
    #     if stack1[-1] == 'q' and a == 'u':
    #         stack1.append(a)
    #     elif stack1[-1] == 'u' and a == 'a':
    #         stack1.append(a)
    #     elif stack1[-1] == 'a' and a == 'c':
    #         stack1.append(a)
    #     elif stack1[-1] == 'c' and a == 'k':
    #         stack1.append(a)
    #         stack1.clear()
    #         cnt+=1
    elif len(stack1) ==0 and a!='q':
        cnt = -1
        break

print(cnt)