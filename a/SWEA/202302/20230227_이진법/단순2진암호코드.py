import sys
sys.stdin = open('input', 'r')

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def checksum(password):
    global even
    global odd
    global check
    for i in range(1,len(password)+1):
        if i%2==0:
            even+=password[i-1]
        else:
            odd +=password[i-1]

    check = odd*3+even
    if check%10==0:
        return even+odd
    else:
        return 0


T = int(input())
conversion = {'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
for tc in range(1,T+1):
    n,m = list(map(int,input().split()))
    digit = []
    password = []
    start = 0
    check = 0
    odd = 0
    even = 0
    cnt = 0
    trash = []
    for _ in range(n):
        board = input()
        cnt += 1

        for i in range(m-1,-1,-1):
            if board[i] == '1':
                start = i
                break

        if start:
            for j in range(start-55,start+1):
                digit.append(board[j])
            print(digit)

        a = list_chunk(digit,7)
        if a:
            break
    for _ in range(n-cnt):
        trash.append(input())

    for w in a:
        password.append(conversion.get(''.join(w)))

    print(password)
    print(f'#{tc}',checksum(password))



# 0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011





