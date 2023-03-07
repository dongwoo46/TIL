import sys
sys.stdin = open('input','r')

n,l = list(map(int,input().split()))
time = 0
arr = [[0,0,1]]+[list(map(int,input().split())) for _ in range(n)]+[[l,0,1]]
for i in range(1,len(arr)):
    d,r,g = arr[i]
    time += (d - arr[i-1][0])
    time += max(0,r - (time%(r+g)))



print(time)


