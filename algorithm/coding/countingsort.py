arr = [0,5,4,3,2,2,8,6]

counts = [0] * (max(arr)+1)

for i in arr:
    counts[i] +=1

for j in range(1,len(arr)):
    counts[i] = counts[i]+ counts[i-1]

temp = [0] * len(arr)

#temp는 인덱스가 0부터 시작하기 때문에 counts보다 인덱스를 하나 낮춰줘야함 ex) counts =[1,4,3,2,5]에서 4는 1이 4번째 자리에 있다는 것임 temp[4]를 하면 인덱스가 0부터 시작하므로 5번째자리에
# 1이들어감 따라서 인덱스를 counts[num]-1해서 인덱스를 하나 낮춰 4번째 자리에 counts[num]값이 들어가도록 함

for num in arr:
    temp[counts[num]-1] = counts[num]
    counts[num]-=1