
def isEmpty():
    return front == rear

def isFull():
    return  (rear+1) % n == front

def enQueue(item, queue):
    global rear
    if isFull():
        print("queue is full")
    else:
        rear = (rear+1)%n
        queue[rear] = item

def deQueue(queue):
    global front
    if isEmpty():
        print("queue is empty")
    else:
        front = (front+1) % n
        return queue[front]

rear = 0
front = 0

T = int(input())
for tc in range(1,T+1):
    n,m = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    bake = [0]*n
    number = [0]


    while True:
        for i in range(n):
            if bake[i] == 0:
                enQueue(deQueue(pizza), bake)
                number[i] = i




        for cheese in bake:
            cheese = cheese//2
            if cheese == 0:
                deQueue(bake)
                enQueue(deQueue(pizza), bake)
                number

        for i in range(n):
            if bake.count(0) == n-1:
                result =












