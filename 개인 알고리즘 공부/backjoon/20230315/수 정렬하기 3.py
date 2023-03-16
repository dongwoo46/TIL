import sys
sys.stdin = open('input','r')
n = int(input())
arr = [int(input()) for i in range(n)]


counts = [0]*(max(arr)+1)

for i in arr:
    counts[i] +=1

for i in range(1, len(counts)):
    counts[i] = counts[i]+counts[i-1]

temp = [0] * len(arr)

for num in arr:
    temp[counts[num]-1] = num
    counts[num] -= 1

sys.stdout.write(temp)