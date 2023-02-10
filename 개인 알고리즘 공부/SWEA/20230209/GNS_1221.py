import sys
sys.stdin = open('input','r')
T = int(input())

str_dict = {'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,'SVN':7, 'EGT':8,'NIN':9,'ZRO':0}
numb_dict = {v:k for k,v in str_dict.items()}

for tc in range(1,T+1):
    a,b = input().split()
    numbers = input().split()

    for i in range(int(b)):
            numbers[i] = str_dict.get(numbers[i])
    numbers.sort()

    for i in range(int(b)):
        numbers[i] = numb_dict.get(numbers[i])

    print(f'#{tc}', *numbers)

'''
def pre_precessing(pattern):
    j = 0 # 앞 글자
    next = [0]*len(pattern)
    for i in range(1, len(pattern)): #뒷 글자
        if pattern[i] == patern[j]:
            next[i] = j + 1
            j += 1
        else:
            j = 0 #다시 맨 앞부터 비교 
            if patter[i] == pattern[j]:
                next[i] = j+1
                i+= 1
    return next 
           
    pass    
def KMP(text, patter):

    #패턴 전처리
    next = pre_preprocessing(pattern)
    i = 0
    j = 0
    cnt = 0
    while i<len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        else:
            if j !=0:
                j = next[j-1]
            else:
                i += 1
        if j == len(pattern):
            count += 1
            j = 0
    return count 
            
    pass
    
pattern_list = ['ZRO','ONE','TWO'...]
T = int(input()
for i in range(T):
    t,N = input().split()
    text = list(input().split()
    
    for i in range(10):
        for j in range(KMP(text, pattern_list[i]))
'''