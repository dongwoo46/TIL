n = int(input())
lst = []
ans = []
try:
    for i in range(1,n):
        lst = list(map(int,str(i)))
        mn = i
        for j in lst:
            mn+=j
        if mn == n:
            ans.append(i)
    print(min(ans))

except:
    print(0)

