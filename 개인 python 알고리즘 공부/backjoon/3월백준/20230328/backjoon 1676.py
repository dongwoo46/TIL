total = 1
n = int(input())
for i in range(1,n+1):
    total *=i
cnt = 0
for i in str(total)[::-1]:
    if i == '0':
        cnt+=1
    else:
        break
print(cnt)