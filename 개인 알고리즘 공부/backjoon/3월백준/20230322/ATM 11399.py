import sys
sys.stdin = open('input', 'r')

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

total_list = [0]*n
total_list[0] = arr[0]
for i in range(1, n):
    total_list[i] = total_list[i-1]+arr[i]
print(sum(total_list))
