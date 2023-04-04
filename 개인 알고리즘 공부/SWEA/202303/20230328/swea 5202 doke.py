import sys
sys.stdin =open('../../../../input')


n = int(input())
schedule = [list(map(int,input().split())) for _ in range(n)]

# for i in range(n):
#     min_idx = i
#     for j in range(i+1,n):
#         if schedule[min_idx][1]> schedule[j][1]:
#             min_idx = j
#     schedule[i],schedule[min_idx] = schedule[min_idx],schedule[i]

cnt = 0
end = 0
schedule.sort(key = lambda x:(x[1],x[0]))
a = sorted(schedule, key=lambda x:x[1])
print(schedule)
print(a)
for s,e in schedule:
    if end<=s:
        cnt+=1
        end = e
print(cnt)



