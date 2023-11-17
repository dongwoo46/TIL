import sys
sys.stdin = open('input','r')

n, k = map(int, input().split())
product = []
for i in range(n):
    w,v = map(int,input().split())
    product.append((w,v))

bag = 0
mx = 0
dp =
