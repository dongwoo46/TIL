import sys
sys.stdin = open('input', 'r')
#values()이용해도됨
bracket_left = ['(','{','[']
#key() 이용해도됨
bracket_right = [')','}',']']

bracket_dict = {')':'(','}':'{',']':'['}

T = int(input())
for tc in range(1,T+1):
    stack = []
    sentence = input()
    #sentence의 각각 원소 하나 씩 탐색
    for bracket in sentence:
        #만약 bracket이 열린괄호면 stack에 넣고
        if bracket in bracket_left:
            stack.append(bracket)
        #만약 bracket이 닫힌괄호고 stack이 비어있으면 탐색 끝 0출력
        elif bracket in bracket_right:
            if not stack:
                print(f'#{tc} 0')
                break
            #bracket이 닫힌괄호인데 stack이 안비어잇을때
            else:
                #stack의 마지막 값과 bracket의 value값이 동일하면 stack pop하기
                if stack[-1] == bracket_dict.get(bracket):
                    stack.pop()
                #아니면 0출력
                else:
                    print(f'#{tc} 0')
                    break
    #for esle구문 위의 출력이 break없이 끝났을때 stack이 남아잇으면 0 아니면 1
    else:
        if len(stack) != 0:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')
