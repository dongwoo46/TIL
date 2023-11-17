# 유니온 파인드 구현하기

# find_set
def  find_set(x): # x가 속한 집합의 대표
    while x!=rep[x]: # x==rep[x]가 될때 까지
        x = rep[x]
    return x

# union(x,y)
def union(x,y): # y의 대표원소가 x의 대표원소를 가르키도록 함
    rep[find_set(y)] = find_set(x)
    # rep[y] = find_set(x) 하면 틀림!!!


#make_set()
rep = [x for x in range(6)]
