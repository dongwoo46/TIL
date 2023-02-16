import sys
sys.stdin = open('input','r')

cry = list(input())
cnt=0
stack1 = []
quack = [0] * len(cry)
while True:
    if sum(quack) == len(cry):
        break

    i

    for i in range(len(cry)):
        if  ('k' in stack1 or not stack1) and cry[i] == 'q':
            if quack[i] ==0:
                a = i
                stack1.append(cry[i])
        if stack1:
            if stack1[-1]=='q' and  cry[i] == 'u':
                if quack[i] == 0:
                    stack1.append(cry[i])
                    quack[i] = 1
                    b = i
            elif stack1[-1]=='u' and cry[i] == 'a':
                if quack[i] == 0:
                    stack1.append(cry[i])
                    quack[i] = 1
                    c = i
            elif stack1[-1]=='a' and cry[i] == 'c':
                if quack[i] == 0:
                    stack1.append(cry[i])
                    quack[i] = 1
                    d = i
            elif stack1[-1]=='c' and cry[i] == 'k':
                if quack[i] == 0:
                    stack1.append(cry[i])
                    quack[i] = 1
                    e = i

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