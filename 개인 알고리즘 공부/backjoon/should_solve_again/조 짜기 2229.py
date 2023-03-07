import sys
sys.stdin = open('../20230305/input', 'r')

n = int(input())
student = list(map(int,input().split()))
max_score = 0



for m in range(1,n+1):
    score = 0
    group = list_chunk(student,m)
    for i in range(len(group)):
        if len(group[i]) ==1:
            score += 0

        else:
            score += max(group[i])-min(group[i])
    max_score = max(score,max_score)
print(max_score)

