import sys
sys.stdin = open('input','r')
input = sys.stdin.readline
n = int(input())
lst1 = list(map(int,input().split()))

m = int(input())
lst2 = list(map(int,input().split()))
result = []
for i in lst2:
    if i in lst1:
        print(1,end=' ')
    else:
        print(0,end=' ')
