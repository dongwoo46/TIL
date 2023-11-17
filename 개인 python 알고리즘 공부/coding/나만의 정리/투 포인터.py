n = 5
m = 5
data = [1,2,3,4,5]

cnt = 1
interval_sum = 0
end = 0

# start를 차례로 증가시키며 반복 (따로 while문 써서 start가 n-1에 도달하면 종료하는 방법도 잇음)
for start in range(n):
    # end를 가능한 만큼 이동
    while interval_sum < m and end< n: # end가 리스트 범위를 벗어나면 안됨
        interval_sum += data[end]
        end +=1
    # 부분합이 m이면 카운트 늘려주기
    if interval_sum ==m:
        cnt+=1
    # 부분합이 m에 도달했으니 start를 증가시키므로 부분합에서 이전 start값 빼주기
    interval_sum -= data[start]