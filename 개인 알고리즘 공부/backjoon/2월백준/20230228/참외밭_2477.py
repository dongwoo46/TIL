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

if board[0][0] == 3 or board[0][0] == 4:
    if len(south) == 2:
        lose_sn = south[1]
    elif len(north) == 2:
        lose_sn = north[1]
    if len(east) == 2:
        lose_ew = east[0]
    elif len(west) == 2:
        lose_ew = west[0]
else:
    if len(south) == 2:
        lose_sn = south[0]
    elif len(north) == 2:
        lose_sn = north[0]
    if len(east) == 2:
        lose_ew = east[1]
    elif len(west) == 2:
        lose_ew = west[1]

lose_ground = lose_ew*lose_sn

print((ground-lose_ground)*n)


