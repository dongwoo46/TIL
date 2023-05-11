
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

lst = [0]*(1000002)
v = 1000001
# n == 1일때는 따로 설정해야함 'IOI'일때 따로 설정 즉 O가 1개일때
for i in range(1,1000001):
    lst[i] = v
    v-=1
# p = 'IOI'+(n-1)*'OI'
cnt = 0
result = []
result_cnt = []
string = ''
for i in s:
    if len(string) == 0:
        if i == 'I':
            string+=i
    else:
        if string[-1] != i:
            string+=i

        else:
            result.append(string)
            result_cnt.append(cnt-n+1)
            string = ''
            cnt = 0
            if i == 'I':
                string+=i
else:
    result.append(string)


print(result)

# OOIOIOIOIIOIIOIOIOIO
# end = len(p)-1
# for start in range(m-len(p)+1):
#
#     if s[start:end+1] == p:
#         cnt+=1
#     end +=1
#
# print(cnt)```