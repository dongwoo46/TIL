import sys
sys.stdin = open('input', 'r')

T = int(input())
for tc in range(1,T+1):
    n,k = list(map(int,input().split()))
    submit = list(map(int,input().split()))
    student = [x for x in range(1,n+1)]

    for i in submit:
        student.remove(i)

    student.sort()
    print(f'#{tc}',*student)


