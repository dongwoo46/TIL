def check(n, arr1, arr2):
    board = [[0] * n for _ in range(n)] # arr1과 arr2를 합쳐서 판별할 새로운 보드 만듦
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1': # 만약 arr1[i][j]나 arr2[i][j]가 1이면 board[i][j]를 1로바꿈
                board[i][j] = 1 # 하나라도 1이면 board는 1
            elif arr1[i][j] == '0' and arr2[i][j] == '0': # 모두 0이면 board = 0
                board[i][j] = 0
    return board


def solution(n, arr1, arr2):
    answer = []
    arr1_2 = [] # arr1을 이진법으로 바꾸엇을대 보드
    arr2_2 = [] # arr2를 이진법으로 바꾸었을때 보드

    for i in arr1: # arr1의 배열에서 이진법으로 바꾸었을때 길이가 n보다 작으면 n만큼 앞에 0을 붙여준다.
        if len(bin(i)[2:]) < n:
            arr1_2.append('0' * (n - len(bin(i)[2:])) + bin(i)[2:])
        else:
            arr1_2.append(bin(i)[2:]) # 만약 이진법의 크기가 n이라면 그대로 넣어줌
    for j in arr2: # 이하 동문
        if len(bin(j)[2:]) < n:
            arr2_2.append('0' * (n - len(bin(j)[2:])) + bin(j)[2:])
        else:
            arr2_2.append(bin(j)[2:])

    board = check(n, arr1_2, arr2_2) # board만들기!

    for i in board: #보드의 한줄 한줄을 돌면서
        string = ''
        for j in i: # 보드의 각각 값이
            if j == 1: # 1이면 '#'이고
                string += '#'
            else: # 0이면 ' ' 빈칸!
                string += ' '
        answer.append(string)

    return answer

# print(solution(n,arr1,arr2))

