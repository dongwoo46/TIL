n = int(input())
cake = [0]*(n+1)
guess_list = [] # 이터 번호
result = []
 # 먹이갯수
eater = int(input())
for i in range(eater):
    a,b = list(map(int,input().split()))
    guess = b-a+1
    guess_list.append(guess)
    cnt = 0
    for j in range(a,b+1):
        if cake[j] == 0:
            cnt+=1
            cake[j] = 1
    result.append(cnt)

print(guess_list.index(max(guess_list))+1)
print(result.index(max(result))+1)

