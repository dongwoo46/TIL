import sys
sys.stdin = open('input','r')
n, k = list(map(int,input().split()))
girl = []
boy = []
cnt = 0
for i in range(n):
    sex, grade = list(map(int,input().split()))
    if sex == 0:
        girl.append(grade)
    else:
        boy.append(grade)
for i in range(1,7):
    if girl.count(i)%k == 0:
        cnt+=girl.count(i)//k
    else:
        cnt +=girl.count(i)//k +1
for i in range(1,7):
    if boy.count(i)%k == 0:
        cnt+=boy.count(i)//k
    else:
        cnt +=boy.count(i)//k +1


print(cnt)

