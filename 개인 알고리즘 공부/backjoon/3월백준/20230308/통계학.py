import sys
sys.stdin = open('input', 'r')
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

d = dict()
for item in arr:
    if item in d:
        d[item] += 1
    else:
        d[item] = 1

m = 0
tmp = list()
for k, v in list(d.items()):
    if v > m:
        tmp = [k]
        m = v
    elif v == m:
        tmp.append(k)
tmp.sort()

# 산술평균
print(round(sum(arr) / N))
# 중앙값
print(arr[N // 2])
# 최빈값
if len(tmp) == 1:
    print(tmp[0])
else:
    print(tmp[1])
# 범위
print(arr[-1] - arr[0])