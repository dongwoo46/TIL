import sys
sys.stdin = open('input', 'r')

cry = list(input())
cnt=0
quack = [0] * len(cry)


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


if len(cry)%5 !=0:
    print(-1)
    exit()

def duck(start):
    global cnt
    first = 0
    check_q = 0
    previous = None
    for i in range(len(cry)):
        if quack[i] == 0 and cry[i] == 'q' and check_q == 0:
            check_q = 1
            previous = cry[i]
            quack[i] = 1
            continue
        elif not quack[i] and cry[i] == 'q' and previous == 'k':
            quack[i] = True
            previous = cry[i]
            continue
            # previous = cry[i]
        if quack[i] == 0 and cry[i] == 'u' and previous == 'q':
            quack[i] = 1
            previous = cry[i]
            continue

        if quack[i] == 0 and cry[i] == 'a' and previous == 'u':
            quack[i] = 1
            previous = cry[i]
            continue

        if quack[i] == 0 and cry[i] == 'c' and previous == 'a':
            quack[i] = 1
            previous = cry[i]
            continue
        if quack[i] == 0 and cry[i] == 'k' and previous == 'c' and first == 0:
            previous = cry[i]
            quack[i] = 1
            cnt+=1
            first = 1
            continue
        elif quack[i] == 0 and cry[i] =='k' and previous == 'c' and first == 1:
            previous = cry[i]
            quack[i] = 1
            continue

for i in range(len(cry)):
    if cry[i] == 'q' and quack[i] == 0:
        duck(i)

if 0 in quack or cnt == 0:
    print(-1)
else:
    print(cnt)