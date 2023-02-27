import sys
sys.stdin = open('input','r')

switch = int(input())
light =[-1] + list(map(int, input().split()))

n = int(input())
a = 0
b = 0
k = 1

for i in range(n):
    sex, numb = list(map(int,input().split()))
    #남자 일때는 numb의 배수만큼 light의 스위치를 바꿔줌
    if sex == 1:
        for i in range(switch):
            if i!=0 and i%numb == 0:
                if light[i] == 1:
                    light[i] = 0
                else:
                    light[i] = 1
    else:
        #numb+-k 가 light의 개수를 벗어나면 종료
        while True:
            if numb+k>=8 and numb-k<0:
                break
            # 만약 벗어나지 않으면
            if numb+k<8 and numb-k>=0:
                # k만큼 numb의 좌우를 살피면서 둘이 값이 같으면 시작점은 numb-k 끝점은 numb+k
                if light[numb+k] == light[numb-k]:
                    a = numb-k
                    b = numb+k
                #만약 둘이가 다르면 a= numb-k+1 b = numb+k+1로 바꿔줌 그리고 반복 종료
                elif light[numb+k] != light[numb-k]:
                    a = numb-k+1
                    b = numb+k-1
                    break
            k += 1

        # 해당 좌우가 같은 값인 범위 내에서 불빛을 바꿔줌
        for j in range(a, b+1):
            if light[j] == 1:
                light[j] = 0
            else:
                light[j] = 1

for i in range(1, switch+1):
    print(light[i], end = " ")
    if i!=0 and i % 20 == 0:
        print()



