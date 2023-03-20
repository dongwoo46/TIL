
n = int(input())
lst = []
ans = []

for i in range(n-9*len(str(n))-1,n):
    lst = list(map(int,str(i)))
    mn = i
    for j in lst:
        mn+=j
    if mn == n:
        ans.append(i)

print(min(ans))





