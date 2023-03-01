import sys
sys.stdin = open('input', 'r')

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

def checksum(password):
    global even
    global odd
    global check
    for i in range(1,8):
        if i%2==0:
            even+=password[i-1]
        else:
            odd +=password[i-1]

    check = odd*3+even+password[-1]
    if check%10==0:
        return even+odd+password[-1]
    else:
        return -1

pw_dict = {'3211':0,'2221':1,'2122':2,'1411':3,'1132':4,'1231':5,'1114':6,'1312':7,'1213':8,'3112':9}

T = int(input())
for tc in range(1,T+1):
    n,m = list(map(int,input().split()))

    password = []

    start = 0
    check = 0
    odd = 0
    even = 0


    for _ in range(n):
        board = list(input())
        sixteen = ''
        res = ''
        mult = 0
        bin_res = ''
        bin_chunk = ''
        cnt = 1
        cnt_list = []
        pw_list = []
        last_ans = 0
        # for i in range(m-1,-1,-1):
        #     if board[i] != '0':
        #         sixteen += board[i]

        for i in range(m):
            if board[i] != '0':
                sixteen += board[i]

        for six in sixteen:
            w = str(bin(int(six,16))).replace('0b', '')
            if len(w) < 4:
                w = '0' * (4 - len(w)) + w
            res = res + w

        if res:
            ans = res.strip('0')
            n = 0
            mult = 0

            if len(ans) % 4 != 0:
                while True:
                    if 4 * n < len(ans) < 4 * (n + 1):
                        mult = n + 1
                        bin_res = '0' * (4 * (mult) - len(ans)) + ans
                        break
                    n += 1

            for i in range(len(bin_res)):
                if i == len(bin_res)-1:
                    if bin_res[i-1] == bin_res[i]:
                        cnt_list.append(cnt)
                    else:
                        cnt_list.append(1)
                elif bin_res[i] == bin_res[i+1]:
                    cnt += 1
                elif bin_res[i] != bin_res[i+1]:
                    cnt_list.append(cnt)
                    cnt = 1

            for list in list_chunk(cnt_list,4):
                for m in list:
                    pw_list.append(m//min(list))

            p_list = [str(x) for x in pw_list]




            for pw in list_chunk(p_list,4):
                password.append(pw_dict.get(''.join(pw)))

            if checksum(password) != -1:
                last_ans = checksum(password)

    print(f'#{tc}', last_ans)





        # 1DB176C588D26EC
        # 0111011 0110001 0111011 0110001 0110001 0001101 0010011 0111011
        # 01110110110001011101101100010110001000110100100110111011