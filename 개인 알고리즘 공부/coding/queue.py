from collections import deque

queue = [0] * 10
front = -1
rear = -1

# enqueue(1)
# rear += 1
# queue[rear] = 1


def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data


def dequeue():
    global front
    front += 1
    return queue[front]

enqueue(1)
enqueue(2)
enqueue(3)
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())

q1 = deque()
q1.append(10)
q1.append(20)
q1.append(30)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())
