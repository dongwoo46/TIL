import sys
sys.stdin = open('input', 'r')

n = int(input())
cnt1 = 0
cnt2 = 0

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1+=1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    global cnt2

    fib = [0]*(n+1)
    fib[1] = fib[2] = 1
    for i in range(3,n+1):
        cnt2 += 1
        fib[i] = fib[i-1]+ fib[i-2]
    return cnt2


print(fib(n))
fibonacci(n)

print(cnt2)
