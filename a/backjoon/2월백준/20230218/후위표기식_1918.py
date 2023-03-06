import sys
sys.stdin = open('input', 'r')
calculation = input()
out_stack = {'+':1,'-':1,'*':2,'/':2,'(':3}
in_stack = {'+':1,'-':1,'*':2,'/':2,'(':0}
stack = []
back = ''
for cal in calculation:
    if cal.isalnum():
        back +=cal
    else:
        if stack:
            if cal == ')':
                while stack and stack[-1] !='(':
                    back += stack.pop()
                stack.pop()

            elif in_stack.get(stack[-1]) < out_stack.get(cal):
                    stack.append(cal)
            elif in_stack.get(stack[-1]) >= out_stack.get(cal):
                while True:
                    if stack: #스택이 남아있고
                        if in_stack.get(stack[-1]) <out_stack.get(cal): #스택안의 갑보다 밖의 값이 더크면 밖에것을 스택에 집어넣고 반복 종료
                            stack.append(cal)
                            break
                        else: #스택 안이 더크면 스택안의 것을 빼와서 back에 추가
                            back += stack.pop()
                    else: #만약 스택이 비어잇으면 해당 연산자를 집어넣고 종료
                        stack.append(cal)
                        break
        else:
            stack.append(cal)

else:
    while stack:
        back += stack.pop()


print(back)