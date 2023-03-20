cal = list(input())
minus = []
plus_numb =[]
minus_numb = []
numb = ''
min_numb = ''
loc = 0
for i in range(len(cal)):
    if cal[i] == '-':
        loc = i
        break
    else:
        if cal[i].isdigit():
            numb+=cal[i]
        else:
            plus_numb.append(numb)
            numb = ''
if numb:
    plus_numb.append(numb)

if loc:
    for j in range(loc+1,len(cal)):
        if cal[j].isdigit():
            min_numb+=cal[j]
        else:
            minus_numb.append(min_numb)
            min_numb = ''
    if min_numb:
        minus_numb.append(min_numb)
res_p = 0
res_m = 0
for a in plus_numb:
    res_p += int(a)
for b in minus_numb:
    res_m += int(b)

print(res_p - res_m)
