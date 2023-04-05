import sys
sys.stdin = open('input','r')

def backtrack(v,lst):
    global cnt
    if v == len(genre):
        for i in range(len(lst)-1):
            if lst[i] == lst[i+1]:
                return
            else:
                cnt+=1
    backtrack(v+1, lst+[genre[v]])
    backtrack(v+1, lst)

T = int(input())
for tc in range(1,T+1):
    n= int(input())
    fashion = [input().split() for _ in range(n)]
    cnt = 0
    genre = []
    for i in range(n):
        genre.append(fashion[i][1])
    backtrack(0,[])
    print(cnt)