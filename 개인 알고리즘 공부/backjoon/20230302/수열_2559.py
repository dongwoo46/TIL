import sys
sys.stdin = open('input', 'r')

n,k = list(map(int,sys.stdin.readline().split()))
degree = list(map(int,sys.stdin.readline().split()))
max_total = 0

for i in range(n):
    total = 0
    m = 0
    while i+m<n and m<k:
        total += degree[i+m]
        m+=1
    if total > max_total:
        max_total = total

print(max_total)