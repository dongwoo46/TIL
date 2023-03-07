p = 'is'#찾을 패턴
t = 'this is a book~!'#전체 텍스트
M = len(p)#찾을 패턴길이
N = len(t)#전체 텍스트 길이
#몇번째에 p와 같은 문자열이 t에 존재하는지
def BruteForce(p,t):
    i = 0#t의 인덱스
    j = 0#p의 인덱스
    while j<len(p) and i<len(t):
        if t[i] != p[j]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == len(p):returni-M#검색성공
    else:return-1#검색 실패
#몇번째에 p와 같은 문자열이 t에 존재하는지
def bf2(p,t,N,M):
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
            else:
                return i
        return -1
#패턴의 개수를 찾고자 할때
def bf2(p,t,N,M):
    cnt = 0
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
            else:
                cnt += 1
                # return i
        return cnt #-1
