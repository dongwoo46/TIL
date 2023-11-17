n = int(input())
location = []
for _ in range(n):
    location.append(list(map(int, input().split())))

location.sort()
for i in range(n-1):
    if location[i][0] > location[i+1][0]:
        location[i], location[i+1] = location[i+1], location[i]

    elif location[i][0] == location[i+1][0]:
        if location[i][1] >location[i+1][1]:
            location[i], location[i+1] = location[i+1], location[i]

for i in range(n):
    print(*location[i])