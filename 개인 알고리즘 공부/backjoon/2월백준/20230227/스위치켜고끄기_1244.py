import sys
sys.stdin = open('input', 'r')

switch = int(input())
light =[-1] + list(map(int, input().split()))

n = int(input())
a = 0
b = 0

def converse(v):
    if light[v] == 1:
        light[v] = 0
    else:
        light[v] = 1

for i in range(n):
    sex, numb = list(map(int,input().split()))
    #남자 일때는 numb의 배수만큼 light의 스위치를 바꿔줌
    if sex == 1:
        for i in range(1,switch+1):
            if i%numb == 0:
                converse(i)
    else:
        converse(numb)
        k = 1
        #numb+-k 가 light의 개수를 벗어나면 종료
        while numb+k<=switch and numb-k>=1:
            if  light[numb+k] == light[numb-k]:
                converse(numb+k)
                converse(numb-k)
            else:
                break
            k += 1


for i in range(1, switch+1):
    print(light[i], end = " ")
    if i % 20 == 0:
        print()



