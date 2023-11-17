from collections import deque
#
# a,b = map(int,input().split())
# q = [x for x in range(1,a+1)]
# result = []
# rear = 0
# front = 0
# while sum(q)!=0:
#     cnt = 0
#     while True:
#         if q[front]!=0:
#             cnt+=1
#         if cnt ==b:
#             break
#         front = (front+1)%7
#     result.append(q[front])
#     q[front]=0
a,b = map(int,input().split())
q = deque(x for x in range(1,a+1))
res = []
while q:
    for i in range(b-1):
        q.append(q.popleft())
    res.append(q.popleft())



print('<'+str(res)[1:-1]+'>')