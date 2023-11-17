def solution(id_list, report, k):
    report_who = [[] for _ in range(len(id_list))]
    report_cnt = {}
    punish = []
    answer = [0] * len(id_list)
    for x in id_list:
        report_cnt[x] = 0

    for r in set(report):
        a, b = r.split()  # a 신고한 사람 b 신고당한 사람
        report_cnt[b] += 1

        if b not in report_who[id_list.index(a)]:
            report_who[id_list.index(a)].append(b)

    for name in report_cnt:
        if report_cnt[name] >= k:
            punish.append(name)
    for i in range(len(report_who)):
        for j in report_who[i]:
            if j in punish:
                answer[i] += 1

    return answer