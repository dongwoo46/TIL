discount = [10, 20, 30, 40]

def solution(users, emoticons):
    # answer = [(이모티콘 가입자수, 이모티콘 매출액)]
    # users = [(할인율,  이모티콘 가입한도)]
    # emoticons = [(각 이모티콘 가격)]
    answer = [0,0]
    dis_list = []
    def backtrack(v):
        nonlocal answer
        if v == len(emoticons): # 이모티콘의 개수만큼 다 탐색하면
            cnt = total = 0
            for i in range(len(users)):
                temp = 0
                for j in range(len(emoticons)):
                    if users[i][0] <=dis_list[j]: # 유저가 원하는 할인율보다 각각의 이모티콘 할인율이 더 크면
                        temp += emoticons[j]*(100-dis_list[j])//100  # temp에 j번째 이모티콘의 가격*할인적용
                if temp>=users[i][1]: # 만약 temp비용이 유저의 이코티콘 플러스 서비스보다 크면
                    cnt+=1 # 이모티콘 서비스 가입
                else:
                    total += temp # 아니라면 이모티콘 구입
            if cnt > answer[0] or (cnt==answer[0] and total>answer[1]):
                # 만약 현재의 cnt가 answer의 cnt보다 크거나 만약 answer의 cnt와 현재 cnt가 같을때
                # total이 answer의 total보다 값이 크면 갱신해준다.!
                answer = [cnt, total]
            return


        for i in range(4): # discount는 4개밖에 없으므로 4개의 할인율만 돈다.
            dis_list.append(discount[i]) # 각각 이모티콘 할인율에 이모티콘 할인율을 넣고
            backtrack(v+1) # 개수를 증가시키고 또 반복
            dis_list.pop() # 빼고 또 반복
    backtrack(0)
    return answer