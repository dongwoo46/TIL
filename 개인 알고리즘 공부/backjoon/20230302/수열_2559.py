import sys
sys.stdin = open('input', 'r')

n,k = list(map(int,sys.stdin.readline().split()))
degree = list(map(int,sys.stdin.readline().split()))


total = sum(degree[:k])
max_total = total

for i in range(n-k):
    total = total - degree[i]+degree[i+k]
    max_total = max(max_total,total)


print(max_total)