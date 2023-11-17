import sys
sys.stdin = open('input','r')

n = int(input())
price = [list(map(int,input().split())) for _ in range(n)]

total = 0

# RGB경우의 수를 3가지로 나눠서 경우를 따져서 해보잡
for i in range(1,n): # i는 집 번호
    #빨간집 선택
    price[i][0] = min(price[i-1][1],price[i-1][2])+price[i][0]
    #초록집 선택
    price[i][1] = min(price[i-1][0],price[i-1][2])+price[i][1]
    #파란집 선택
    price[i][2] = min(price[i-1][0],price[i-1][1])+price[i][2]

print(min(price[n-1]))

