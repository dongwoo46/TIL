import sys
sys.stdin = open('input','r')
T = int(input())

for tc in range(1,T+1):

    word = list(input())
    temp = []
    for i in range(0,len(word)):
        if not temp:
            temp.append(word[i])
        else:
            if temp[-1] == word[i]:
                temp.pop()
            elif temp[-1] != word[i]:
                temp.append(word[i])

    print(f'#{tc} {len(temp)}')