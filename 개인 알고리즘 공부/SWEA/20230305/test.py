n= int(input())

ten = []
cnt=0

while True:
    print(set(ten))
    if len(set(ten)) == 10:
        break
    cnt += 1
    numb = list(map(int,str(n*cnt)))
    for i in numb:
        ten.append(i)