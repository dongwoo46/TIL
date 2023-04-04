T = int(input())
for tc in range(1,T+1):
    n = int(input())
    ans = -1
    start = 1
    end = n
    while start<=end:
        mid = (start+end)//2
        triple = mid*mid*mid
        if triple == n:
            ans = mid
            break
        if triple > n:
            end = mid-1
        if triple<n:
            start = mid+1

    print(f'#{tc}', ans)

