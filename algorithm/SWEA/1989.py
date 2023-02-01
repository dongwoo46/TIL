T = int(input())
 
for t in range(1,T+1):
    word = list(input())
    rev_word = []
    for item in word[::-1]: #[::-1] 역으로 슬라이싱
        rev_word.append(item)
 
    if word == rev_word:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')