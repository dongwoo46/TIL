import sys
sys.stdin = open('input','r')

def  isEmpty():
    return front == rear

def isFull():
    return (rear+1) % len(queue) == front

def enqueue(item):
    global rear
    if isFull():
        print("Queue_FUll")
    else:
        rear = (rear+1) % len(queue)
        queue[rear] = item

def dequeue():
    global front
    if isEmpty():
        print("queue_empty")
    else:
        front = (front+1) % len(queue)




# T = int(input())
# for tc in range(1,T+1):
#     n, m = list(map(int,input().split()))
#     word = list(map(str,input().split()))
#     queue = [0]*(n+1)
#     front = 0
#     rear = 0
#     for i in range(n):
#         enqueue(word[i])
#
#     for _ in range(m):
#         dequeue()
#         enqueue(queue[front])
#
#     print(f'{tc} {queue[front+1]}')

#교수님 풀이
t = int(input())
for tc in range(1,t+1):
    while not isEmpty():
        dequeue()
    res = 0
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    queue = [0] * (n+1)
    for a in arr: #array원소를 하나씩 가져옴
        enqueue(a)

    for _ in range(m%n):
        enqueue(dequeue())
    res = dequeue()

    print(f'#{tc} {res}')


