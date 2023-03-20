import sys
sys.stdin = open('input', 'r')
n = int(input())

numb = 0
max_cnt = 0
ans = []

for i in range(n,n//2-1,-1):
    k = 0
    cnt = 2
    result = [n]
    result.append(i)
    while True:
        numb = result[k]-result[k+1]
        if numb<0:
            break
        else:
            result.append(numb)
            cnt +=1
            k+=1

    if cnt>max_cnt:
        ans = result
        max_cnt = len(result)

print(max_cnt)
print(*ans)

