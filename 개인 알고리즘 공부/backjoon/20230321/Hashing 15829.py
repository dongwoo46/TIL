# dic = { a:1,b:2,c:3,d:4,e:5,f:6,g:7,h:8\
import sys
sys.stdin = open('input','r')

alpha = list('abcdefghijklmnopqrstuvwxyz')
numb = [x for x in range(1,27)]
dic = {name:value for name,value in zip(alpha,numb)}
n = int(input())
s = list(input())
total = 0
for i in range(len(s)):
    total+=dic[s[i]]*(31**i)
print(total%1234567891)