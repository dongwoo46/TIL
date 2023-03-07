import sys
sys.stdin = open('input','r')
def cho(left,left_cnt):
    if len(left) == 1:
        if left[0] == 'C':
            left_cnt[0] += +1
        elif left[0] == 'H':
            left_cnt[1] += 1
        elif left[0] == 'O':
            left_cnt[2] += +1
    else:
        for i in range(len(left)):
            if i == len(left) - 1 and left[i].isdigit():
                continue
            elif i == len(left) - 1 and not left[i].isdigit():
                if left[i] == 'C':
                    left_cnt[0] += 1
                elif left[i] == 'H':
                    left_cnt[1] += 1
                elif left[i] == 'O':
                    left_cnt[2] += 1
            else:
                if left[i] == 'C':
                    if left[i + 1].isdigit():
                        left_cnt[0] += int(left[i + 1])
                    elif left[i+1] == 'C':
                        left_cnt[0] += 1
                    else:
                        left_cnt[0] += 1
                elif left[i] == 'H':
                    if left[i + 1].isdigit():
                        left_cnt[1] += int(left[i + 1])
                    elif left[i + 1] == 'H':
                        left_cnt[1] += 1
                    else:
                        left_cnt[1] += 1
                elif left[i] == 'O':
                    if left[i + 1].isdigit():
                        left_cnt[2] += int(left[i + 1])
                    elif left[i + 1] == 'H':
                        left_cnt[2] += 1
                    else:
                        left_cnt[2] += 1
    return left_cnt

chemical = list(input())
#C H O
l_cnt = [0]*3
m_cnt = [0]*3
r_cnt = [0]*3
result = []
p = 0
e = 0
for i in range(len(chemical)):
    if chemical[i] == '+':
        p = i
    elif chemical[i] == '=':
        e = i
left = chemical[0:p]
mid = chemical[p+1:e]
right = chemical[e+1:]
ans_l = cho(left,l_cnt)
ans_m = cho(mid,m_cnt)
ans_r = cho(right,r_cnt)

# print(l_cnt,m_cnt,r_cnt)

for i in range(1,11):
    for j in range(1,11):
        for k in range(1,11):
            if (i*int(l_cnt[0]) + j*int(m_cnt[0])) == k*int(r_cnt[0]) and (i*int(l_cnt[1])+j*int(m_cnt[1]))==k*int(r_cnt[1]) and (i*int(l_cnt[2])+j*int(m_cnt[2]))==k*int(r_cnt[2]):
                result.append((int(i),int(j),int(k)))

result.sort()


print(*result[0])
