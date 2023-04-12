def check(n, arr1, arr2):
    board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                board[i][j] = 1
            elif arr1[i][j] == '0' and arr2[i][j] == '0':
                board[i][j] = 0
    return board


def solution(n, arr1, arr2):
    answer = []
    arr1_2 = []
    arr2_2 = []

    for i in arr1:
        if len(bin(i)[2:]) < n:
            arr1_2.append('0' * (n - len(bin(i)[2:])) + bin(i)[2:])
        else:
            arr1_2.append(bin(i)[2:])
    for j in arr2:
        if len(bin(j)[2:]) < n:
            arr2_2.append('0' * (n - len(bin(j)[2:])) + bin(j)[2:])
        else:
            arr2_2.append(bin(j)[2:])

    board = check(n, arr1_2, arr2_2)

    for i in board:
        string = ''
        for j in i:
            if j == 1:
                string += '#'
            else:
                string += ' '
        answer.append(string)

    return answer
n = 5
arr1 = [9,20,28,18,11]
arr2 = [30,1,21,17,28]
print(solution(n,arr1,arr2))

