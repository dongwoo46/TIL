def solution(today, terms, privacies):
    contract ={}
    today_lst = list(map(int,today.split('.')))
    answer = []

    for term in terms:
        s, l = term.split()  # 약관종류, 몇개월인지 놔눠
        contract[s] = int(l)*28 #일로계산해서 넣어버려
    for i in range(len(privacies)): # 날짜와 약관종류 돌면서
        date, s = privacies[i].split() # 날짜와 약관종류 적고
        date_lst = list(map(int, date.split('.'))) # 날짜는 .으로 나누고
        # 년 월 일 각각 다 계산해서 일수로 바꿔줌
        year = (today_lst[0] - date_lst[0])*336
        month = (today_lst[1]-date_lst[1])*28
        day = today_lst[2] - date_lst[2]
        # 그래서 총 몇일이 지났는지 확인
        total = year+month+day
        # 만약 계약 유효기간보다 total이 크거나 같으면 정보 삭제
        if contract[s] <= total:
            answer.append(i+1)
    return answer