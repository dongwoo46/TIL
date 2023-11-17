import sys
sys.stdin = open('input', 'r')
n= int(input())
start = 666
while n!=0:
    if '666' in str(start):
        n-=1
    start+=1
print(start-1)
