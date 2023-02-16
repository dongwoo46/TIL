import sys
sys.stdin = open('input','r')
for tc in range(1,11):
    n = int(input())
    calculation = input()
    numb = []
    operator = []
    for cal in calculation:
        if cal.isdigit():
            numb.append(int(cal))
        else:
            if operator:
                if cal == '+' and operator[-1] == '+':
                    operator.append(cal)
                elif cal == '*' and operator[-1] == '*':
                    operator.pop()
                    numb.append(int(numb.pop()*numb.pop()))
                    operator.append(cal)
                elif cal == '*' and operator[-1] == '+':
                    operator.append(cal)
                elif cal == '+' and operator[-1] == '*':
                    operator.pop()
                    numb.append(int(numb.pop()*numb.pop()))
                    operator.append(cal)
            else:
                operator.append(cal)
    else:
        if len(numb)>=2 and operator:
            for _ in range(len(operator)):
                if operator[-1] == '+':
                    operator.pop()
                    numb.append(int(numb.pop()) + int(numb.pop()))
                else:
                    operator.pop()
                    numb.append(int(numb.pop())*int(numb.pop()))
            print(f'#{numb.pop()}')
        elif len(numb) == 1:
            print(f'#{numb.pop()}')
