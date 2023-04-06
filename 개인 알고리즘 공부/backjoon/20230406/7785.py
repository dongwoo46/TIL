import sys
sys.stdin = open('input','r')
n = int(input())
result = []
for i in range(n):
    name, order = input().split()
    if order == 'enter':
        result.append(name)
    elif order == 'leave':
        result.remove(name)
result.sort(reverse=True)
for i in result:
    print(i)
