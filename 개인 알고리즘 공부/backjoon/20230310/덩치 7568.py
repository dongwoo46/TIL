import sys
sys.stdin = open('input','r')

n = int(input())
tall =[]
result = [0]*(n)
size = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    rank = 1
    for j in range(n):
        if size[i][0] <size[j][0] and size[i][1]<size[j][1]:
            rank +=1
    result[i] = rank

print(*result)
