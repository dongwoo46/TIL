import sys
sys.stdin = open('input', 'r')
m,n = list(map(int,input().split()))
time = int(input())
h_list= [0]
w_list = [0]
ans_h = []
ans_w = []
result = 0
h = 0
w = 0
for i in range(time):
    a,b = list(map(int,input().split()))
    if a == 0:
        h_list.append(b)
    else:
        w_list.append(b)
h_list.append(n)
w_list.append(m)
h_list.sort()
w_list.sort()
for i in range(len(h_list)-1):
    h = h_list[i+1]-h_list[i]
    ans_h.append(h)
for j in range(len(w_list)-1):
    w = w_list[j+1]-w_list[j]
    ans_w.append(w)

for x in ans_h:
    for y in ans_w:
        result = max(result,x*y)

print(result)
