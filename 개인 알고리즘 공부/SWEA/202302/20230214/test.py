import sys
sys.stdin = open('input', 'r')
def tile(n):
    f = [0] * (n + 1)
    f[10] = 1
    f[20] = 3

    for i in range(30, n + 10, 10):
        f[i] = f[i - 10] + f[i - 20] * 2
    return f[n]


for tc in range(1, int(input()) + 1):
    n = int(input())
    print(f'#{tc} {tile(n)}')