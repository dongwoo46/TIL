import sys
import copy
sys.stdin = open('input', 'r')

all_short = []
check = 0
for _ in range(9):
    all_short.append(int(input()))



for i in range(8):
    for j in range(i+1,9):
        if sum(all_short) - all_short[i]-all_short[j] == 100 :
            all_short.remove(all_short[i])
            all_short.remove(all_short[j-1])
            check = 1
            break
    if check:
        break

all_short.sort()
for k in all_short:
    print(k)

