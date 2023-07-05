import sys
sys.stdin = open('input', 'r')

n = input()
m = int(input())
broken = list(map(int,input().split()))
long = len(n)
button = [x for x in range(10)]
cnt = 0
lst = []
numb = ''
for i in broken:
    button.remove(i)


def backtracking(v):
    global numb
    if v == long:
        lst.append(numb)
        return
    for i in button:
        numb = numb+str(i)
        backtracking(v+1)
        numb = numb[:-1]

mn = 1e9
ans = 0
backtracking(0)
for i in lst:
    print(int(n))
    print(int(i))
    print(abs(int(n)-int(i)))
    if abs(int(n)-int(i))<mn:
        ans =abs(int(n)-int(i))

# print(ans)

# n과 가장 가까운 번호 만들기
# 1. 사용할수 있는 버튼이랑 숫자가 맞으면 끼워 넣기!

