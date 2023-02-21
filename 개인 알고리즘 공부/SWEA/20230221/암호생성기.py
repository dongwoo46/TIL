for _ in range(1,11):
    tc = int(input())
    queue = list(map(int,input().split()))
    cnt = 0
    while queue[-1] >0:
        # if cnt == 6:
        #     cnt = 1
        cnt = cnt%5+1
        queue.append(queue.pop(0) - cnt)
        # cnt += 1

    if queue[-1]<0:
        queue[-1] = 0

    print(f'#{tc}', *queue)
