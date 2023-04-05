import sys
sys.stdin = open('input','r')

T = int(input())
for tc in range(1,T+1):
    n= int(input())
    dic = {}
    for i in range(n):
        style, body = input().split()
        if body not in dic:
            dic[body] = 1
        else:
            dic[body] +=1
    ans = 1
    for item in dic.values():
        ans*=item+1
    print(ans-1)