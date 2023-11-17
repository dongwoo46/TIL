import sys
sys.stdin = open('input', 'r')
n = int(input())

building = [0]* 1001
max_h = 0
max_l = 0

for _ in range(n):
    l, h = list(map(int,input().split()))
    building[l]=h
    if h>max_h:
        max_h = h
        max_l = l

total = 0
c_height = 0

for i in range(max_l+1):
    if c_height<building[i]:
        c_height = building[i]
    total += c_height

c_height = 0
for j in range(1000,max_l,-1):
    c_height = max(c_height,building[j])
    total += c_height

print(total)



