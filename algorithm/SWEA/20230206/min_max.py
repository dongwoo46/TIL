# import sys
# sys.stdin = open("input.txt", "r")

#min값 max값 구해서 빼는 함수 만들고
def min_max(numbers):
    maxV = numbers[0]
    minV = numbers[0]
    for i in range(len(numbers)):
        if maxV <= numbers[i]:
            maxV = numbers[i]
        if minV >= numbers[i]:
            minV = numbers[i]
    return maxV-minV

#T만큼 실행
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = min_max(numbers)
    print(f'#{tc} {result}')
