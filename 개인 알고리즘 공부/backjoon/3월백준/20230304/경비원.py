import sys
sys.stdin = open('input', 'r')
def direction(a,b):
    if a == 1:
        a = 0
    elif a == 2:
        a = n
    elif a == 3:
        a = b
        b = 0

    else:
        a = b
        b = m

    return a,b

def cal_dis():
    global distance
    if b == 0 and guard[0][1] == m:
        distance += m+min((guard[0][0]+a),((n-a)+(n-guard[0][1])))
    elif a == 0 and  guard[0][0] == n:
        distance += n + min((guard[0][1]+b),(m-b)+(m-guard[0][1]))
    elif b == m and guard[0][1] == 0:
        distance += m+min((guard[0][0]+a),((n-a)+(n-guard[0][1])))
    elif a == n and guard[0][0] == 0:
        distance += n + min((guard[0][1]+b),(m-b)+(m-guard[0][1]))
    else:
        distance += abs(a-guard[0][0]) + abs(guard[0][1]-b)
    return distance

m,n = list(map(int,input().split()))
k = int(input())
store = []
guard = []
distance = 0


for i in range(k+1):
    if i == k:
        x,y = list(map(int,input().split()))
        x,y = direction(x,y)
        guard.append((x,y))
    else:
        store.append(list(map(int,input().split())))

for j in range(k):
    a,b = store[j]
    a,b = direction(a,b)
    if guard[0][0] == a and guard[0][1] != b:
        distance += abs(guard[0][1]-b)
    elif guard[0][1] == b and guard[0][0] != a:
        distance += abs(guard[0][0]-a)
    else:
        cal_dis()
print(distance)






