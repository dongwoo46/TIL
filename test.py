import sys

sys.stdin = open('input')
for _ in range(1,int(input())+1):
      n,k=map(int,input().split())
      lst=list(map(int,input().split()))
      cnt=0
      for i in range(1<< n):
            s=0
            for j in range(n):
                  print(1 << j)
                  if i & (1 << j):

                        s += lst[j]
            if s == k:
                  cnt+=1

      print('#{} {}'.format(_,cnt))