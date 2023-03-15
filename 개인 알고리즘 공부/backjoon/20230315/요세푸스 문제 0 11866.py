from collections import deque

def isEmpty():
    return front == rear
def isFull():
    return (rear+1) % len(q) == front
def deQueue():
    global front
    if isEmpty():
        return
    else:
        front = (front+b) % len(q)
        return q[front]

a,b = map(int,input().split())
q =[0] + [x for x in range(1,a+1)]
result = [0]*(a+1)
rear = 0
front = 0
while True:
    if isEmpty():
        break
    for i in range(1,a+1):




print(str(result))
print('<'+str(result)[1:-1]+'>')