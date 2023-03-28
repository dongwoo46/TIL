# 데이터의 개수 n과 전체 데이터 선언
n = 5
data = [1,2,3,4,5]

#접두사합 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세번째수부터 네번째수까지)
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1])