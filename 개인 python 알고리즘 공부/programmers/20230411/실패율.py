def solution(N, stages):
    user = len(stages)
    challenge = [0] * (N+2)  # 해당 스테이지에 도전 중인 사람들
    temp = []
    answer = []
    for i in stages:
        if i > N:
            continue
        challenge[i] += 1

    for i in range(1, N+2):
        if user:
            temp.append((challenge[i] / user, i))  # 실패율 , 도전자수
            user -= challenge[i]
        else:
            temp.append((0, i))


    temp.sort(key=lambda x: x[0], reverse=True)
    for fail, stage in temp:
        if stage > N:
            continue
        else:
            answer.append(stage)

# 실패율 = counter/ user

    return answer

N = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(N,stages))