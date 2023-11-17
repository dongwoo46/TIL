def  pizza():
    for i in range(n):
        if bake[i][0] == 0:
            bake.append((pizza.pop(0), 1))

# 어떻게 풀까
# queue에 집어넣는다. 화덕에 n개만큼 집어넣음
# 화덕이 구울게 있는 동안 만약 i번째 위치에 치즈가 있으면 치즈//2
# 치즈가 0이되면 꺼내는 피자 기록
# 입력을 받을 때 몇번 피자였는지 따로 기록 ex)튜플  (7,1) (2,2) ...
bake = []
T = int(input())
for tc in range(1,T+1):
    n, m = list(map(int,input().split()))
    pizza = list(map(int,input().split()))
    number = 1
    if not bake:
        for i in range(n):
            bake.append((pizza.pop(0), number))
            number += 1
        else:
            if bake[i]:
                bake[i][0] = bake[i][0]//2
    else:
        for i in range(n):
            if bake[i][0] == 0:
                bake.append((pizza.pop(0)), number)
                number += 1
        else:
            bake[i][0] == bake[i]



