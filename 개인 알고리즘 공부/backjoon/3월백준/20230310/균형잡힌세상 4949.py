import sys
sys.stdin = open('input', 'r')
while True:
    sentence = list(input())
    bracket = {')':'(','}':'{',']':'['}
    stack = []
    if len(sentence) == 1 and sentence[0] == '.':
        break

    for s in sentence:
        if s in bracket.values():
            stack.append(s)
        elif s in bracket.keys():
            if not stack:
                print('no')
                break
            else:
                if stack[-1] == bracket.get(s):
                    stack.pop()
                else:
                    print('no')
                    break
    else:
        if stack:
            print('no')
        else:
            print('yes')

