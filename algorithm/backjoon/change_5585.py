n = int(input())

cnt = 0
change = 1000-n

while change>0:
    if change>=500:
        cnt += change//500
        change = change%500
    elif 500>change>= 100:
        cnt += change//100
        change = change%100
    elif 100>change>= 50:
        cnt += change//50
        change = change%50
    elif 50>change>= 10:
        cnt += change//10
        change = change%10
    elif 10>change>= 5:
        cnt += change//5
        change = change%5
    elif change>= 1:
        cnt += change//1
        change = change%1

# print(cnt)
# while change>=500:
#     change = change - 500
#     cnt += 1
#
# while change>=100:
#     change = change - 100
#     cnt +=1

# while change >= 50:
#     change -=50
#     cnt +=1
#
# while change>=10:
#     change -= 10
#     cnt +=1
#
# while change>=5:
#     change-=5
#     cnt +=1
#
# while change>=1:
#     change -=1
#     cnt+=1
#
# print(cnt)
