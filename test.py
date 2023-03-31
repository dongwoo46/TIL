lst = [1, 2, 3, 4, 5]
n = 5

# 만들수 있는 순열의 경우의수 = 5! = 5 * 4 * 3 * 2 * 1 = 120

# swap 방식(자리교환) 순열 만들어 보기
# 현재 idx 번째 숫자를 다른 누구와 바꿀 것인지 정해 준다.
cnt = 0


def perm(idx):
    global cnt

    # 종료 조건
    if idx == n:
        cnt += 1
        # 자리를 바꾸고 난 후에 하고싶은 작업을 여기에 코드로 작성
        print(lst)
        return

    # 재귀 호출
    # 현재 idx 번째 숫자와 자리를 바꿀 i번째 다른 숫자를 결정
    # 다른 숫자의 인덱스 i는 중복을 피하기 위해 idx보다 커야 한다.
    for i in range(idx, n):
        # idx와 자리를 바꿀 i를 정했다면 자리를 바꾸고 진행
        lst[idx], lst[i] = lst[i], lst[idx]
        # 자리를 바꾸고 다음 자리를 또 정하러 재귀 호출
        perm(idx + 1)
        # i번째에 대해서 자리를 바꿔보고 다른 i에 대해서 자리를 바꿔야
        # 하니까 원상복귀 시키고 진행
        lst[idx], lst[i] = lst[i], lst[idx]


perm(0)
print(cnt)
