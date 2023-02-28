n = int(input())
acc = int(n*(n**2+1)/2)
map_list = []
su = n-1
width = 0
length = 0
diagonal1 = 0
diagonal2 = 0
magic_width = ''
magic_diagonal1 =''
magic_diagonal2 = ''
magic_length = ''
overlap = 0


for i in range(n):
    map_list.append(list(map(int,input().split())))
    width = sum(map_list[i])
    if width != acc:
        magic_width = 'Fail'
    else:
        magic_width = 'Pass'
        

for i in range(n):
    diagonal1 += map_list[i][i]
    # print(diagonal1)
if diagonal1 != acc:
    magic_diagonal1 = 'Fail'
else:
    magic_diagonal1 = 'Pass'

for i in range(n):
    diagonal2 += map_list[i][i+su]
    su -=2   
if diagonal2 != acc:
    magic_diagonal2 = 'Fail'
else:
    magic_diagonal2 = 'Pass'   


for j in range(n):
    length = 0
    for i in range(n):
        length += map_list[i][j]
        if length != acc:
            magic_length = 'Fail'
        else:
            magic_length = 'Pass'
            
for numb in map_list:
    if map_list.count(numb) >1:
        overlap = 'Fail'
    else:
        overlap = "Pass"

if magic_length == 'Pass' and magic_diagonal2 =='Pass' and magic_diagonal1 == 'Pass' and magic_width =='Pass' and overlap == 'Pass':
    print('TRUE')
else:
    print('FALSE')