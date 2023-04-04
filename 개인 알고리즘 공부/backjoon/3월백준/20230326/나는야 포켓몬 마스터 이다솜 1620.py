import sys
sys.stdin = open('../20230325/input', 'r')

n, m = map(int, input().split())
poket = [input() for _ in range(n)]
numb = [x for x in range(1,n+1)]

dic = {idx:value for idx,value in zip(numb,poket)}
dic_r = {value:idx for idx,value in zip(numb,poket)}

for i in range(m):
    a = input()
    if a.isdigit():
        print(dic[int(a)])
    else:
        print(dic_r[a])

