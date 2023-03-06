import sys
sys.stdin = open('input', 'r')
for tc in range(1,11):
    left = []
    n, password = list(input().split())

    for numb in password:
        if not left:
            left.append(numb)
        elif left:
            if left[-1] == numb:
                left.pop()
            else:
                left.append(numb)


    print(f'#{tc}', ''.join(left))
