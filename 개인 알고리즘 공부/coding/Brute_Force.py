p = 'is' #찾을 패턴
t = 'this is a book~!' #전체 텍스트
M = len(p) #찾을 패턴길이
N = len(t) #전체 텍스트 길이

def BruteForce(p,t):
    i = 0 #t의 인덱스 , t=long
    j = 0 #p의 인덱스, p = short
    while j<len(p) and i<len(t):
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == len(p): return i-M #검색성공
    else: return -1 #검색 실패