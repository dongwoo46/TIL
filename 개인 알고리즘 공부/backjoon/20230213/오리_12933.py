import sys
sys.stdin = open('input','r')

cry = list(input())
cnt=0
stack1 = []
quack = [0] * len(cry)
while True:
    if sum(quack) == len(cry):
        break

    for i in range(len(cry)):
        stack1.clear()
        if cry[i] == 'q':
            if quack[i] !=0:
                a = i
                stack1.append(cry[i])
        elif 'q' in stack1 and  cry[i] == 'u':
            if quack[i] != 0:
                stack1.append(cry[i])
                b = i
        elif 'u' in stack1 and cry[i] == 'a':
            if quack[i] != 0:
                stack1.append(cry[i])
                c = i
        elif 'a' in stack1 and cry[i] == 'c':
            if quack[i] != 0:
                stack1.append(cry[i])
                d = i
        elif 'c' in stack1 and cry[i] == 'k':
            if quack[i] != 0:
                stack1.append(cry[i])
                e = i
        if ''.join(stack1) == 'quack':
            quack[a] = 1
            quack[b] = 1
            quack[c] = 1
            quack[d] = 1
            quack[e] = 1
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