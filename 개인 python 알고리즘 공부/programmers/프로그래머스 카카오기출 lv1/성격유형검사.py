def solution(survey, choices):
    dic_team = {"A": 'N', 'C': 'F', 'J': 'M', 'R': 'T', 'N': 'A', 'F': 'C', 'M': 'J', 'T': 'R'}
    lst = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    dic = {x: 0 for x in lst}
    answer = ''

    for i in range(len(survey)):
        if choices[i] == 1:
            dic[survey[i][0]] += 3
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 7:
            dic[survey[i][1]] += 3

    for i in ['R', 'C', 'J', 'A']:
        if dic[i] > dic[dic_team[i]]:
            answer += i
        elif dic[i] < dic[dic_team[i]]:
            answer += dic_team[i]
        else:
            answer += i


    return answer