import sys
sys.stdin = open('input','r')
input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))
value = [0]
temp = 0
for i in range(n):
    temp +=arr[i]
    value.append(temp)
for i in range(m):
    s, e = map(int,input().split())
    print(value[e]-value[s-1])
