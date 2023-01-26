T = int(input())


for test_case in range(1,T+1):
    one_count = 0
    cnt = 0
    board = []
    one_count_length = []
    one_count_width = []
    n, m = map(int,input().split())


    for j in range(n):
        board.append(list(map(int,input().split())))

# board = [input().split() for _ in range(n)]

    for i in range(n):
        one_count = 0
        for j in range(n):
            if board[i][j] == 1:
                one_count +=1
            else:
                one_count = 0
            one_count_width.append(one_count)
            
            
    for i in one_count_width:
        if i>=m:   
            if i == m:
                cnt += 1
            elif i == m+1 :
                cnt -=1
        else:
            continue

         
            
    for i in range(n):
        one_count = 0
        for j in range(n):
            if board[j][i] == 1:
                one_count +=1
            else:
                one_count = 0
            one_count_length.append(one_count)


    for i in one_count_length:
        if i>=m:   
            if i == m:
                cnt += 1
            elif i == m+1 :
                cnt -=1
        else:
            continue 
            
            
    print(f'#{test_case} {cnt}')
    


