import sys
sys.stdin = open('input', 'r')

n = int(input())
# 번호표
student = list(map(int,input().split()))
ans = []
# ㅑdx + 1을 해ㅜ저야함
for idx, value in enumerate(student):
    ans.insert(value,idx+1)

for i in ans[::-1]:
    print(i,end=' ')
print()