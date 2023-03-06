# import sys
# sys.stdin = open("input.txt", "r")

#max - min 함수만들기
def max_min_sub(numbers):
    maxV = numbers[0] #리스트의 첫값을 MaxV로 저장
    minV = numbers[0] # ''           minV로 ''
    for i in range(len(numbers)): #numbers의 개수만큼 반복실행 해서 각각 maxV값과 minV값을 구함
        if maxV<=numbers[i]:
            maxV = numbers[i]
        if minV>= numbers[i]:
            minV = numbers[i]
    return maxV - minV

#구간합 m칸마다 반복해서 더해서 리스트에 집어넣는다 그걸로  max_min_sub함수 이용해서 최대 빼기 최소구함
def prefix_sum(numb):
    value_list = [] # 빈 리스트를 만듦
    for i in range(n): #n만큼 반복실행 하고 m개의 합을 저장할 value 변수를 만듦
        value = 0
        if i>n-m: #n-m이 되면 반복을 멈춤 ex) n=6 m=3이면 6-3일때 3개 더하는게 끝남
            break
        else:
            for j in range(m):  # m만큼 반복실행하고 value에 각각 리스트의 3개씩 더한 값을 저장해 value_list에 저장
                value += numb[i+j]
            value_list.append(value)
    return max_min_sub(value_list) #value_list에서 최대 최소값을 뺀 것을 구함

#T만큼 반복실행
T = int(input())
for tc in range(1,T+1):
    n, m = list(map(int, input().split()))
    numb = list(map(int, input().split()))
    result = prefix_sum(numb)
    print(f'#{tc} {result}')