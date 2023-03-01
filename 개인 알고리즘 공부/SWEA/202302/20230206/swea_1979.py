T = int(input())


for test_case in range(1,T+1):
    one_count = 0
    cnt = 0
    board = []
    one_count_length = []
    one_count_width = []
    n, m = map(int, input().split())

    #board에 사각형 판을 입력받아서 만듦
    for j in range(n):
        board.append(list(map(int, input().split())))

    # board = [input().split() for _ in range(n)]

    #n만큼 반복 실행한다.
    for i in range(n):
        #1을 count한다
        one_count = 0
        #만약 board칸이 1이라면(흰색이라면) one_count를 +1 해줌 => 1인 칸이 몇개인지 확인하는 과정
        for j in range(n):
            if board[i][j] == 1:
                one_count +=1
            else:
                one_count = 0
            #가로로 1이 몇개인지 샌것을 one_count_width에 넣어줌
            one_count_width.append(one_count)
    #만약 one_count_width의 값이 크거나 같은 값중에서 one_count_width의 값이 m값과 같으면 cnt를 1늘려준다. 만약 i가 m보다 더 크면 cnt를 빼준다.(why 가로 한줄의 연속된 1의 개수를 세는데 만약 m보다 크면
    # 칸이 딱 맞지 않고 큰 칸이 되서 안맞음 그래서 m보다 큰값이 나오는 라인은 삭제해주는 것
    for i in one_count_width:
        if i >= m:
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
        if i >= m:
            if i == m:
                cnt += 1
            elif i == m+1 :
                cnt -=1
        else:
            continue 

    print(f'#{test_case} {cnt}')
    


