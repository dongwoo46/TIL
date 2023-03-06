cal = input()
cal_list = []
stack = []
for i in cal:
    if i.isnumeric():
        cal_list.append(i)
    else:
        stack.append(i)
for i in range(len(stack)):
    cal_list.append(stack.pop())

for j in cal_list:
    print(j, end= '')


