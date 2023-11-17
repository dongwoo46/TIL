a,b = map(int,input().split())
ans = 1
bot = 1
for i in range(b):
    ans = ans*a
    bot = bot*b
    b -=1
    a -=1
print(int(ans/bot))