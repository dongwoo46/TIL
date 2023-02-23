import sys
sys.stdin = open('input','r')

def postorder(node):
    if node:
        postorder(left[node])
        postorder(right[node])
        cal.append(data[node])
    return cal

for tc in range(1,11):
    v =int(input())
    left = [0] * (v+1)
    right = [0] * (v+1)
    data = [0] * (v+1)
    parent = [0] * (v+1)
    cal = []
    stack = []
    for i in range(v):
        #부모, 해당 값 , 왼쪽자식, 오른쪽자식
        temp = input().split()
        if len(temp) == 4:
            left[int(temp[0])] = int(temp[2])
            right[int(temp[0])] = int(temp[3])
            data[int(temp[0])] = temp[1]
            parent[int(temp[2])] = int(temp[0])
            parent[int(temp[3])] = int(temp[0])
        else:
            data[int(temp[0])] = temp[1]

    result = postorder(1)
    for i in result:
        if i.isdigit():
            stack.append(i)
        else:
            if i == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a+b)
            elif i == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b - a)
            elif i == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(a * b)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b // a)
    print(f'#{tc}',stack.pop())
