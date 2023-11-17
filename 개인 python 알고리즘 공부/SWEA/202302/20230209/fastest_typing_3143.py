import sys

sys.stdin = open('input', 'r')

def change_word(long, short):
    temp = '*'

    for i in range(len(long)-len(short)+1):
        if long[i:i+len(short)] == short:
            for j in range(i,i+len(short)):
                long[j] = temp
    return long


    # short가 long에 몇개 들어있는가 체크용
    # for i in range(len(long)-len(short)+1):
    #     for j in range(len(short)):
    #         if long[i+j] != short[j]:
    #             break
    #         elif long[i+j] == short[j]:
    #             same +=1
    #
    #     if same == len(short):
    #         cnt += 1

def pre_precessing(pattern):
    j = 0  # 앞 글자
    next = [0] * len(pattern)
    for i in range(1, len(pattern)):  # 뒷 글자
        if pattern[i] == pattern[j]:
            next[i] = j + 1
            j += 1
        else:
            j = 0  # 다시 맨 앞부터 비교
            if pattern[i] == pattern[j]:
                next[i] = j + 1
                i += 1
    return next

    pass

def KMP(text, pattern):
    # 패턴 전처리
    next = pre_precessing(pattern)
    i = 0
    j = 0
    cnt = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = next[j - 1]
            else:
                i += 1
        if j == len(pattern):
            cnt += 1
            j = 0
    return cnt

print(KMP('anaana', 'ana'))

# T = int(input())
#
# for tc in range(1, T + 1):
#     a, b = input().split()
#     change = a.replace(b, "*")
#
#     print(f'#{tc} {len(change)}')

    # cnt = 0
    # change = 0
    # ans =0
    # a, b = input().split()
    # ans_word = change_word(a,b)
    # for i in len(ans_word):
    #     if ans_word[i] == 0:
    #         cnt +=1
    #
    # for j in range(len(ans_word)-1):
    #     if ans_word[i] == '*' and ans_word[i+1] != '*':
    #         change += 1
    #
    # ans = cnt - ((len(b)-1)*change)
    #
    # print(f'#{tc} {ans}')
