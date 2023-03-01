import sys
sys.stdin = open('input','r')

n = int(input())
north = []
south = []
east = []
west = []
board = []
ground = 0
max_ew = 0
max_sn = 0
lose_ew = 0
lose_sn = 0
lose_ground = 0


for _ in range(6):
    direction, length = list(map(int, input().split()))
    board.append((direction,length))

    if direction == 1:
        east.append(length)
    elif direction == 2:
        west.append(length)
    elif direction == 3:
        south.append(length)
    else:
        north.append(length)

if max(east) > max(west):
    max_ew = max(east)
else:
    max_ew = max(west)

if max(south) > max(north):
    max_sn = max(south)
else:
    max_sn = max(north)

ground = max_sn*max_ew

for idx,value in enumerate(board):
    if value[1] == max_sn:
        lose_ew = abs(board[(idx-1)%6][1] - board[(idx+1)%6][1])
    if value[1] == max_ew:
        lose_sn = abs(board[(idx-1)%6][1]-board[(idx+1)%6][1])

lose_ground = lose_ew*lose_sn

print((ground-lose_ground)*n)


