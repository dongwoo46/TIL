import sys
sys.stdin = open('input','r')

n = int(input())
member = []
for _ in range(n):
    member.append(input().split())

member.sort(key = lambda x:int(x[0]))
# for i in range(0,len(member)):
#     for j in range(0,len(member)-i-1):
#         if member[j][0] >member[j+1][0]:
#             member[j], member[j+1] = member[j+1], member[j]

for memb in member:
    print(' '.join(memb))
