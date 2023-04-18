dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}  # 맞은개수 : 등수


def solution(lottos, win_nums):  # 민우로또번호, 당첨번호
    cnt = 0
    cnt0 = 0
    for i in lottos:
        if i == 0:
            cnt0 += 1
        for j in win_nums:
            if i == j:
                cnt += 1

    answer = [dic[cnt0 + cnt], dic[cnt]]
    return answer