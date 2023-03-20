arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 모든 범위를 포함하는 리스트 선언 (모든 값 0으로 초기화)
count = [0] * (max(arr)+1)

for i in range(len(arr)):
    count[arr[i]]+=1 # 각데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

