import sys
sys.stdin = open('input','r')
# n -> 2*n / a->2*1타일 수 /b -> 2*2타일수
n,a,b=map(int,input().split())
a_box=list(map(int,input().split()))
b_box=list(map(int,input().split()))
a_box.sort(reverse=True)
b_box.sort(reverse=True)
box_num=[(n-i*2,i) for i in range(n//2+1)]
print(box_num)
result=0

for an,bn in box_num:
    max_num=0
    if an>a or bn>b: continue
    for i in range(an):
        max_num+=a_box[i]
    for i in range(bn):
        max_num+=b_box[i]
    if max_num>result:
        result=max_num
print(result)