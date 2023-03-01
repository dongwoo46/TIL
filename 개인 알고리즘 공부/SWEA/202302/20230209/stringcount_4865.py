import sys
sys.stdin = open('input', 'r')

#str1 찾을거 str2 텍스트
def alphabet_count(str1,str2):

    max_cnt = 0
    for s1 in str1:
        cnt = 0
        for s2 in str2:
            if s1 == s2:
                cnt += 1
            if max_cnt <cnt:
                max_cnt = cnt
    return max_cnt


T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    ans = alphabet_count(str1, str2)
    print(f'#{tc} {ans}')




