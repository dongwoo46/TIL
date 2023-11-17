import sys
sys.stdin = open('input')
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr_1 = sorted(arr)
dic = dict(enumerate(set(arr_1)))
dic_r = {value:idx for idx,value in dic.items()}

result = []
for x in arr:
    result.append(dic_r.get(x))
print(*result)



