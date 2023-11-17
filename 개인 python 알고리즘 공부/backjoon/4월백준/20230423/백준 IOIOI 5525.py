import sys
sys.stdin = open('input', 'r')
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
stack = []


for i in range(m):
    if len(stack) == 0:
        if s[i]=='I':
            stack.append(s[i])
    else:
        if s[-1] != s[i]:
            stack.append(s[i])
        stack = []






p = 'IOI'+(n-1)*'OI'
cnt = 0

end = len(p)-1
for start in range(m-len(p)+1):

    if s[start:end+1] == p:
        cnt+=1
    end +=1

print(cnt)