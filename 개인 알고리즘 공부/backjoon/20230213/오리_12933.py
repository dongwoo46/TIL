import sys
sys.stdin = open('input','r')

cry = list(input())
cnt=0
stack1 = []
quack = [0] * len(cry)

def duck(start):
    global cnt
    first = 0

    for i in range(len(cry)):
        if cry[i] == 'q' and quack[i] == 0:
            stack1.append(cry[i])
            quack[i] = 1
            # previous = cry[i]
        elif stack1[-1] == 'q'  and  cry[i] == 'u':
            if quack[i] == 0:
                quack[i] = 1
                stack1.append(cry[i])

        elif stack1[-1] == 'u' and cry[i] == 'a':
            if quack[i] == 0:
                stack1.append(cry[i])
                quack[i]
                c = i
        elif 'a' in stack1 and cry[i] == 'c':
            if quack[i] == 0:
                stack1.append(cry[i])
                d = i
        elif 'c' in stack1 and cry[i] == 'k':
            if quack[i] == 0:
                stack1.append(cry[i])
                e = i
    if stack1:
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


print(cnt)