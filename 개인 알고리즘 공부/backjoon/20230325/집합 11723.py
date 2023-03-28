# 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
#
# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다.

import sys
sys.stdin = open('input','r')
input = sys.stdin.readline
s = 0
n = int(input())
for _ in range(n):
    order = input().split()
    if order[0] == "add":
        s = s|(1<<int(order[1]))
        continue
    elif order[0] == "remove":
        s = s & ~(1<<int(order[1]))
        continue
    elif order[0] == "check":
        if s&(1<<int(order[1])):
            print(1)
        else:
            print(0)
        continue
    elif order[0] == "toggle":
        s = s^(1<<int(order[1]))
        continue
    elif order[0] == "empty":
        s = 0
        continue
    elif order[0] == "all":
        s = (1<<21)-1
        continue

# import sys
# m = int(input())
# s = 0b0

# for _ in range(m):
#   cmd = list(map(str, sys.stdin.readline().split()))
#   if len(cmd) == 2:
#     n = int(cmd[1])
#     cmd = cmd[0]
#   else:
#     cmd = cmd[0]
#
#   if cmd == "check":
#     if s & (1 << n): # s and n
#       print(1)
#     else: # ~(s and n)
#       print(0)
#   if cmd == "add":
#     s = s | (1 << n) # s or n
#   if cmd == "remove":
#     s = s & ~(1 << n) # s or ~n
#   if cmd == "toggle":
#     s = s ^ (1 << n) # s xor n
#   if cmd == "all":
#     s = (1 << 21) - 1
#   if cmd == "empty":
#     s = 0b0





