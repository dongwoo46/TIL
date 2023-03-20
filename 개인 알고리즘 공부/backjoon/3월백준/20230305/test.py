def list_chunk(lst,a):
    return [lst[i:i+a] for i in range(0,len(lst),a)]

a = [x for x in range(10)]
b =[ x for x in range(-1,-10,-1)]
print(b)
