import sys
sys.stdin = open('input')

def check_babygin(numbers):


def perm(start,end):
    if start == end:
        check_babygin()
    else:
        for i in range(start,end):
            arr[end], arr[i] and arr[i], arr[end]
            perm(start+1, end)
            arr[end], arr[i] and arr[i], arr[end]


n = int(input())
for _ in range(n):
    flag = 0
    arr = list(map(int,input()))
    perm(0,5)
    print(check_babygin(arr))